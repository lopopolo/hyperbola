const path = require('path');
const glob = require('glob-all');
const webpack = require('webpack');
const CleanWebpackPlugin = require('clean-webpack-plugin');
const ExtractTextPlugin = require('extract-text-webpack-plugin');
const FaviconsWebpackPlugin = require('favicons-webpack-plugin');
const FileManagerPlugin = require('filemanager-webpack-plugin');
const PurgeCSSPlugin = require('purgecss-webpack-plugin');

const isProduction = process.env.NODE_ENV === 'production';

// process.traceDeprecation = true;

function plugins(isProd) {
  const p = [
    new CleanWebpackPlugin(
      [
        './dist/*',
        './document-root/**/*.ico',
        './document-root/**/*.png',
      ],
      {
        exclude: ['.gitignore'],
      },
    ),
    new webpack.optimize.ModuleConcatenationPlugin(),
    new ExtractTextPlugin('[name].bundle.css'),
    new PurgeCSSPlugin({
      // Give paths to parse for rules. These should be absolute!
      paths: glob.sync([
        path.join(__dirname, 'hyperbola/templates/*.html'),
        path.join(__dirname, 'hyperbola/*/templates/*.html'),
      ]),
      styleExtensions: ['.css'],
      minimize: isProd,
      keyframes: false,
    }),
    new FaviconsWebpackPlugin({
      logo: './src/img/logo.favicon.svg',
      prefix: 'icons/',
      persistentCache: false,
      // which icons should be generated (see https://github.com/haydenbleasel/favicons#usage)
      icons: {
        android: false,
        appleIcon: true,
        appleStartup: false,
        coast: false,
        favicons: true,
        firefox: false,
        opengraph: false,
        twitter: false,
        yandex: false,
        windows: false,
      },
    }),
    new FileManagerPlugin({
      onEnd: [
        {
          move: [
            { source: './dist/icons/favicon.ico', destination: './document-root/favicon.ico' },
            { source: './dist/icons/apple-touch-icon.png', destination: './document-root/apple-touch-icon.png' },
          ],
        },
        {
          delete: [
            './dist/icons',
          ],
        },
      ],
    }),
  ];
  if (isProd) {
    p.push(new webpack.optimize.UglifyJsPlugin());
  }
  return p;
}

module.exports = {
  entry: {
    main: ['main', 'hyperbola.browser'],
  },
  output: {
    path: path.resolve(__dirname, './dist'),
    filename: '[name].bundle.js',
  },
  resolve: {
    modules: ['node_modules', 'src'],
    extensions: ['.js'],
  },
  plugins: plugins(isProduction),
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        loader: 'babel-loader',
      },
      {
        test: /\.css$/,
        use: ExtractTextPlugin.extract({
          fallback: 'style-loader',
          use: 'css-loader',
        }),
      },
      {
        test: /\.(jpe?g|png|ttf|eot|woff(2)?)(\?[a-z0-9=&.]+)?$/,
        use: {
          loader: 'base64-inline-loader',
          options: {
            limit: 2000,
            name: '[name].[ext]',
          },
        },
      },
      {
        test: /\.(svg)(\?[a-z0-9=&.]+)?$/,
        use: [
          {
            loader: 'base64-inline-loader',
            options: {
              limit: 2000,
              name: '[name].[ext]',
            },
          },
          {
            loader: 'svgo-loader',
          },
        ],
      },
    ],
  },
};
