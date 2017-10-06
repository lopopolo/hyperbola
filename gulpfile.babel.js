import del from 'del';
import favicons from 'gulp-favicons';
import filter from 'gulp-filter';
import gulp from 'gulp';
import gutil from 'gulp-util';
import imagemin from 'gulp-imagemin';
import runSequence from 'run-sequence';
import svg2png from 'gulp-svg2png';
import webpack from 'webpack-stream';

const webpackConfig = require('./webpack.config.js');

gulp.task('default', ['build']);

gulp.task('build', (callback) => {
  runSequence(
    'clean',
    ['build:webpack', 'img'],
    callback,
  );
});

gulp.task('clean', () => del([
  './dist/**',
  '!./dist/**/.gitignore',
  './document-root/**/*.ico',
  './document-root/**/*.png',
]));

gulp.task('build:webpack', () => gulp.src('./src/main.js')
  .pipe(webpack(webpackConfig))
  .on('error', (errorInfo) => {
    gutil.log(errorInfo.toString());
    this.emit('end');
  })
  .pipe(gulp.dest('./dist')));

gulp.task('img', ['img:favicon']);

gulp.task('img:favicon', () => gulp.src('./src/img/logo.favicon.svg')
  .pipe(svg2png({ width: 160 * 3, height: 160 * 3 }))
  .pipe(favicons({
    icons: {
      android: false,
      appleIcon: true,
      appleStartup: false,
      coast: false,
      favicons: true,
      firefox: false,
      windows: false,
      yandex: false,
    },
    url: 'https://hyperbo.la/',
    display: 'standalone',
    orientation: 'portrait',
    replace: true,
  }))
  .pipe(filter(['favicon.ico', 'apple-touch-icon.png']))
  .pipe(imagemin())
  .pipe(gulp.dest('./document-root')));
