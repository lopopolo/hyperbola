function convertDates() {
  var spans = document.getElementsByTagName("span");
  for (var i=0; i < spans.length; i++) {
    var span = spans[i];
    if (span.className == "date") {
      var d = new Date(1000*parseInt(span.getAttribute("utc-seconds")));
      span.innerHTML = printDate(d);
    }
  }
}

function printDate(date) {
  var ret = "";
  ret += padTo2(date.getHours());
  ret += ":";
  ret += padTo2(date.getMinutes());
  ret += " ";
  //ret += "tzname";
  //ret += " ";
  ret += monthToNameMap[date.getMonth()];
  ret += " ";
  ret += padTo2(date.getDate());
  ret += " ";
  ret += date.getFullYear();
  return ret;
}

function padTo2(num) {
  if (num < 10 && num >= 0) {
    return "0" + num;
  }
  return "" + num;
}

var monthToNameMap = {
  0  : "jan",
  1  : "feb",
  2  : "mar",
  3  : "apr",
  4  : "may",
  5  : "jun",
  6  : "jul",
  7  : "aug",
  8  : "sep",
  9  : "oct",
  10 : "nov",
  11 : "dec"
}

window.onload = convertDates;
