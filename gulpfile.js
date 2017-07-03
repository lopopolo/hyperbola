var del = require("del");
var favicons = require("gulp-favicons");
var filter = require("gulp-filter");
var gulp = require("gulp");
var imagemin = require("gulp-imagemin");
var svg2png = require("gulp-svg2png");

gulp.task("default", ["build"]);

gulp.task("build", ["clean", "img"]);

gulp.task("clean", function () {
    return del([
        "./dist/**",
        "!./dist/**/.gitignore",
    ]);
});

gulp.task("img", ["clean", "img:favicon"]);

gulp.task("img:favicon", ["clean"], function () {
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
