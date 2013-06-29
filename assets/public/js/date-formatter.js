var HyperbolaDateFormatter = {
  printDate : function(date) {
    var ret = "";
    ret += this.padTo2(date.getHours());
    ret += ":";
    ret += this.padTo2(date.getMinutes());
    ret += " ";
    ret += this.monthToNameMap[date.getMonth()];
    ret += " ";
    ret += this.padTo2(date.getDate());
    ret += " ";
    ret += date.getFullYear();
    return ret;
  },
  padTo2 : function(num) {
    if (num < 10 && num >= 0) {
      return "0" + num;
    }
    return "" + num;
  },
  monthToNameMap : {
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
  },
}

