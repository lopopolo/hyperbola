var autoprefixer = require("autoprefixer");
var colorguard = require("colorguard");
var cssnano = require("cssnano");
var del = require("del");
var compiler = require("google-closure-compiler-js").gulp();
var gulp = require("gulp");
var concat = require("gulp-concat");
var eslint = require("gulp-eslint");
var htmlhint = require("gulp-htmlhint");
var imagemin = require("gulp-imagemin");
var postcss = require("gulp-postcss");
var purify = require("gulp-purifycss");
var rename = require("gulp-rename");
var filterStream = require("postcss-filter-stream");
var stylefmt = require("stylefmt");

gulp.task("default", ["build"]);

gulp.task("build", ["clean", "css", "js", "html", "img"]);

gulp.task("clean", function () {
    return del([
        "./static/dist/**",
        "!./static/dist",
        "!./static/dist/.gitignore",
    ]);
});

gulp.task("css", ["clean"], function () {
    var processors = [
        autoprefixer({browsers: ["last 1 version"]}),
        stylefmt(),
        filterStream("**/vendor/**", colorguard()),
        cssnano(),
    ];
    return gulp.src(["./static/src/vendor/bootstrap-css-only/css/bootstrap.css", "./static/src/css/sitewide.css"])
        .pipe(purify(["./app/hyperbola/**/templates/*.html"]))
        .pipe(postcss(processors))
        .pipe(concat("css/sitewide.css"))
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
            jsOutputFile: "lifestream-date-formatter.js",
        }))
        .pipe(rename(function (path) {
            path.basename += ".generated.min";
        }))
        .pipe(gulp.dest("./app/hyperbola/lifestream/templates"));
});

gulp.task("js:copy", [
    "js:copy:retinajs",
]);

gulp.task("js:copy:retinajs", ["clean"], function () {
    return gulp.src("./static/src/vendor/retina.js/dist/retina.min.js")
        .pipe(gulp.dest("./static/dist/js"));
});

gulp.task("html", ["clean", "html:lint"]);

gulp.task("html:lint", function () {
    return gulp.src("./bin/**/*.html")
        .pipe(htmlhint())
        .pipe(htmlhint.failReporter());
});

gulp.task("img", ["clean", "img:copy"]);

gulp.task("img:copy", ["clean"], function () {
    return gulp.src("./static/src/img/artifact/**/*")
        .pipe(imagemin())
        .pipe(gulp.dest("./static/dist/img"));
});
