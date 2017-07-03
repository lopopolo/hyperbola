var del = require("del");
var favicons = require("gulp-favicons");
var filter = require("gulp-filter");
var gulp = require("gulp");
var imagemin = require("gulp-imagemin");
var runSequence = require("run-sequence");
var svg2png = require("gulp-svg2png");
var webpack = require("webpack-stream");

gulp.task("default", ["build"]);

gulp.task("build", function(callback) {
    runSequence(
        "clean",
        ["build:webpack", "img"],
        callback
    );
});

gulp.task("clean", function () {
    return del([
        "./dist/**",
        "!./dist/**/.gitignore",
    ]);
});

gulp.task("build:webpack", function() {
    return gulp.src("./src/main.js")
        .pipe(webpack(require("./webpack.config.js"), require("webpack")))
        .on("error", function(errorInfo) {
            console.log(errorInfo.toString());
            this.emit("end");
        })
        .pipe(gulp.dest("./dist"));
});

gulp.task("img", ["img:favicon"]);

gulp.task("img:favicon", function () {
    return gulp.src("./src/img/logo.favicon.svg")
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
        .pipe(gulp.dest("./dist"));
});
