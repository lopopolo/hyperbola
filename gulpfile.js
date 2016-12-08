var gulp = require("gulp");
var concat = require("gulp-concat");
var del = require("del");
var eslint = require("gulp-eslint");
var postcss = require("gulp-postcss");
var purify = require("gulp-purifycss");
var autoprefixer = require("autoprefixer");
var colorguard = require("colorguard");
var cssnano = require("cssnano");
var filterStream = require("postcss-filter-stream");
var stylefmt = require("stylefmt");

gulp.task("default", ["build"]);

gulp.task("build", ["clean", "css", "js", "img"]);

gulp.task("clean", function () {
    return del([
        "./app/hyperbola/dist/**",
        "!./app/hyperbola/dist",
        "!./app/hyperbola/dist/.gitignore",
    ]);
});

gulp.task("css", ["clean"], function () {
    var processors = [
        autoprefixer({browsers: ["last 1 version"]}),
        stylefmt(),
        filterStream("**/vendor/**", colorguard()),
        cssnano(),
    ];
    return gulp.src(["./app/hyperbola/static/vendor/bootstrap-css-only/css/bootstrap.css", "./app/hyperbola/static/css/sitewide.css"])
        .pipe(purify(["./app/hyperbola/**/templates/*.html"]))
        .pipe(postcss(processors))
        .pipe(concat("css/sitewide.css"))
        .pipe(gulp.dest("./app/hyperbola/dist"));
});

gulp.task("js", ["clean", "js:lint", "js:copy"]);

gulp.task("js:lint", function () {
    return gulp.src(["**/*.js", "!**/*.min.js", "!node_modules/**", "!**/vendor/**", "!virtualenv/**", "!assets/**"])
        .pipe(eslint())
        .pipe(eslint.format())
        .pipe(eslint.failAfterError());
});

gulp.task("js:copy", [
    "js:copy:retinajs",
]);

gulp.task("js:copy:retinajs", ["clean"], function () {
    return gulp.src("./app/hyperbola/static/vendor/retina.js/dist/retina.min.js")
        .pipe(gulp.dest("./app/hyperbola/dist/vendor/retina.js/dist"));
});

gulp.task("img", ["clean", "img:copy"]);

gulp.task("img:copy", ["clean"], function () {
    return gulp.src("./app/hyperbola/static/img/artifact/**/*")
        .pipe(gulp.dest("./app/hyperbola/dist/img/artifact"));
});
