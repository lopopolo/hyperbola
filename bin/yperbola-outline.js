#!/usr/bin/env node

const { Console } = console;
const out = new Console(process.stdout, process.stderr);
const TextToSVG = require("text-to-svg");
const textToSVG = TextToSVG.loadSync("/Library/Fonts/Brush Script.ttf");

const attributes = {fill: "#28dcdc", stroke: "#28dcdc"};
const options = {fontSize: 40, anchor: "middle", attributes: attributes};

out.warn(textToSVG.getMetrics("yperbola", options));
const svg = textToSVG.getPath("yperbola", options);

out.log(svg);
