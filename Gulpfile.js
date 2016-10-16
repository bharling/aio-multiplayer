'use-strict';


var gulp = require('gulp');
var sass = require('gulp-sass');
var coffee = require('gulp-coffee');
var gutil = require('gulp-util');
// var bourbon_paths = require('bourbon').includePaths;
var livereload = require('gulp-livereload');

// gulp.task('sass', function () {
// 	return gulp.src('./static/scss/**/*.scss')
// 		.pipe(sass({includePaths: bourbon_paths}).on('error', sass.logError))
// 		.pipe(gulp.dest('./static/css'))
// 		.pipe(livereload());
// });

gulp.task('coffee', function () {
	gulp.src('./static/coffee/**/*.coffee')
		.pipe(coffee().on('error', gutil.log))
		.pipe(gulp.dest('./static/js'))
		.pipe(livereload());
});


gulp.task('default', function () {
	livereload.listen();
	// gulp.watch('./static/scss/**/*.scss', ['sass']);
	gulp.watch('./static/coffee/**/*.coffee', ['coffee'])
});