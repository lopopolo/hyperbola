var autoprefixer = require("autoprefixer");
var colorguard = require("colorguard");
var cssnano = require("cssnano");
var del = require("del");
var compiler = require("google-closure-compiler-js").gulp();
var gulp = require("gulp");
var bower = require("gulp-bower");
var concat = require("gulp-concat");
var eslint = require("gulp-eslint");
var favicons = require("gulp-favicons");
var filter = require("gulp-filter");
var htmlhint_inline = require("gulp-htmlhint-inline");
var imagemin = require("gulp-imagemin");
var postcss = require("gulp-postcss");
var purify = require("gulp-purifycss");
var rename = require("gulp-rename");
var svg2png = require("gulp-svg2png");
var merge = require("merge-stream");
var filterStream = require("postcss-filter-stream");
var stylefmt = require("stylefmt");

gulp.task("default", ["build"]);

gulp.task("build", ["clean", "css", "js", "html", "img"]);

gulp.task("clean", function () {
    return del([
        "./static/dist/**",
        "!./static/dist",
        "!./static/dist/.gitignore",
        "./document-root/**/*.ico",
        "./document-root/**/*.png"
    ]);
});

gulp.task("bower", function () {
    return bower({cmd: "update"});
});

gulp.task("css", ["clean", "bower"], function () {
    var processors = [
        autoprefixer({browsers: ["last 1 version"]}),
        stylefmt(),
        filterStream("**/vendor/**", colorguard())
    ];
    return gulp.src(["./static/src/vendor/bootstrap-css-only/css/bootstrap.css", "./static/src/css/sitewide.css"])
        .pipe(purify(["./app/hyperbola/**/templates/*.html"]))
        .pipe(postcss(processors))
        .pipe(concat("css/sitewide.css"))
        .pipe(postcss([cssnano()]))
        .pipe(gulp.dest("./static/dist"));
});

gulp.task("js", ["clean", "js:lint", "js:compile", "js:copy"]);

gulp.task("js:lint", function () {
    return gulp.src(["**/*.js", "!**/*.min.js", "!node_modules/**", "!**/vendor/**", "!virtualenv/**", "!assets/**"])
        .pipe(eslint())
        .pipe(eslint.format())
        .pipe(eslint.failAfterError());
});

gulp.task("js:compile", function () {
    return gulp.src("./static/src/js/lifestream-date-formatter.js")
        .pipe(compiler({
            compilationLevel: "ADVANCED_OPTIMIZATIONS",
            warningLevel: "VERBOSE",
            jsOutputFile: "lifestream-date-formatter.js"
        }))
        .pipe(rename(function (path) {
            path.basename += ".generated.min";
        }))
        .pipe(gulp.dest("./app/hyperbola/lifestream/templates"));
});

gulp.task("js:copy", ["js:copy:retinajs"]);

gulp.task("js:copy:retinajs", ["clean", "bower"], function () {
    return gulp.src("./static/src/vendor/retina.js/dist/retina.min.js")
        .pipe(gulp.dest("./static/dist/js"));
});

gulp.task("html", ["clean", "html:lint"]);

gulp.task("html:lint", function () {
    return gulp.src(["./bin/**/*.html", "./app/**/*.html"])
        .pipe(htmlhint_inline({
            ignores: {
                "{% load staticfiles": "%}"
            },
            patterns: [
                {
                    match: /\{% extends .+? %}/g,
                    replacement: "<!doctype html>"
                },
                {
                    match: /\{% load hyperbola_lifestream_tags imagekit %}/g,
                    replacement: "<!doctype html>"
                },
                {
                    match: /\{% (url|static) .+? %}/g,
                    replacement: "https://example.com"
                },
                {
                    match: /\{\{ .+? }}/g,
                    replacement: "foo.bar"
                }
            ]
        }))
        .pipe(htmlhint_inline.reporter())
        .pipe(htmlhint_inline.reporter("fail"));
});

gulp.task("img", ["clean", "img:favicon", "img:logo"]);

gulp.task("img:favicon", ["clean"], function () {
    return gulp.src("./static/src/img/logo.favicon.svg")
        .pipe(svg2png({width: 160* 3, height: 160 * 3}))
        .pipe(favicons({
            icons: {
                android: false,
                appleIcon: true,
                appleStartup: false,
                coast: false,
                favicons: true,
                firefox: false,
                windows: false,
                yandex: false
            },
            url: "https://hyperbo.la/",
            display: "standalone",
            orientation: "portrait",
            replace: true
        }))
        .pipe(filter(["favicon.ico", "apple-touch-icon.png"]))
        .pipe(imagemin())
        .pipe(gulp.dest("./document-root"));
});

gulp.task("img:logo", ["clean"], function () {
    var logo1x = gulp.src("./static/src/img/logo.header.svg")
        .pipe(svg2png({width: 230, height: 80}));
    var logo2x = gulp.src("./static/src/img/logo.header.svg")
        .pipe(svg2png({width: 230 * 2, height: 80 * 2}))
        .pipe(rename(function (path) {
            path.basename += "@2x";
        }));
    return merge(logo1x, logo2x)
        .pipe(imagemin())
        .pipe(gulp.dest("./static/dist/img"));
});
