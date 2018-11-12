from invoke import Collection, task


def terraform_output(ctx, *, module, prop):
    with ctx.cd("terraform/app-prod-pdx"):
        result = ctx.run(f"terraform output -module={module} {prop}")
        return result.stdout.strip()


@task
def init(ctx):
    ctx.run("pre-commit install")
    ctx.run("pre-commit install-hooks")
    ctx.run("poetry install")
    ctx.run("yarn install")


@task
def fixtures(ctx):
    ctx.run("vagrant provision --provision-with fixtures app-local", pty=True)


@task
def generate_secret_key(_ctx):
    from django.core.management.utils import get_random_secret_key

    print(get_random_secret_key())


@task(help={"bump": "Version part to bump. One of {major, minor, patch}."})
def release(ctx, bump="minor"):
    ctx.run(f"bumpversion {bump}")
    ctx.run("git push")
    ctx.run("git push --tags")


@task
def clean(ctx, bytecode=True, node=False):
    ctx.run("find . -name '.DS_Store' -delete")
    ctx.run("rm -rf *.egg *.egg-info .cache .coverage .tox build dist docs/build htmlcov")
    if bytecode:
        ctx.run(r"find . -type d -name __pycache__ -exec rm -rf {} +")
        ctx.run("find . -type f -name '*.pyc' -or -name '*.pyo' -delete")
    if node:
        ctx.run("rm -rf node_modules")


@task
def ami(ctx):
    import os
    import random
    from dotenv import load_dotenv

    load_dotenv()
    vpc = terraform_output(ctx, module="network", prop="vpc_id")
    subnet = random.choice(
        terraform_output(ctx, module="network.management", prop="build_subnet_ids").split(",")
    )
    instance_profile = terraform_output(ctx, module="base", prop="app_instance_profile")
    os.environ.setdefault("BUILD_VPC_ID", vpc)
    os.environ.setdefault("BUILD_SUBNET_ID", subnet)
    os.environ.setdefault("BUILD_INSTANCE_PROFILE", instance_profile)

    ctx.run("packer build packer/app.json", pty=True)


@task
def update_launch_template(ctx):
    with ctx.cd("terraform/app-prod-pdx"):
        ctx.run("terraform apply", pty=True)


@task
def cycle_asg(ctx):
    asg = terraform_output(ctx, module="backend", prop="backend_asg")
    ctx.run(f"./bin/cycle_asg --asg-name {asg}", pty=True)


@task(post=[ami, update_launch_template, cycle_asg], default=True)
def deploy(_ctx):
    print("Initiating deploy")


@task(post=[update_launch_template, cycle_asg])
def rollback(ctx):
    ctx.run("git revert --no-edit HEAD")


@task
def finalize(ctx, dry_run=False):
    ctx.run("./bin/deregister_ami --dry-run")
    if not dry_run:
        ctx.run("./bin/deregister_ami --execute")


namespace = Collection(
    init,
    fixtures,
    generate_secret_key,
    clean,
    release,
    Collection("deploy", deploy, ami, update_launch_template, cycle_asg, rollback, finalize),
)
namespace.configure({"run": {"echo": True}})
