/**
 * @param {string} S
 * @return {number}
 */
var minFlipsMonoIncr = function (S) {
    var str1 = S;
    var pre = '0';
    var zero = 0;
    var one = 0;
    var zeroOne = 0;
    var dic = {zero: 0, one: 0, zeroOne: 0};
    var start = 0;
    var end = str1.length - 1
    while (str1[start] == '0' || str1[end] == '1') {
        if (str1[start] == '0') {
            start += 1;
        }
        if (str1[end] == '1') {
            end -= 1;
        }
    }
    for (var i = start; i <= end; i++) {
        if (zero == 0) {//1部分
            if (str1[i] == pre) {
                zero += 1
            } else {
                one += 1
            }
        } else {//0部分
            if (str1[i] == pre) {
                zero += 1;
            } else {
                var tmpZero = dic.zero + one;
                var tmpOne = Math.min(dic.one, dic.zeroOne) + zero;
                var tmoZeroOne = Math.min(dic.zero, dic.one, dic.zeroOne) + zero;
                dic.zero = tmpZero;
                dic.one = tmpOne;
                dic.zeroOne = tmoZeroOne;
                //console.log(str1,dic);
                zero = 0;
                one = 1;
            }
        }
    }
    dic.zero += one;
    dic.one = Math.min(dic.one, dic.zeroOne) + zero;
    dic.zeroOne = Math.min(dic.zero, dic.one, dic.zeroOne) + zero;
    return Math.min(dic.zero, dic.one, dic.zeroOne)
};

var minFlipsMonoIncr1 = function (S) {
    const n = S.length
    let f1 = 0
    let f0 = 0
    let g1 = 0, g0 = 0
    for (let i = 0; i < n; i++) {
        if (i == 0) {
            if (S[i] == '0') {
                f0 = 0;
                f1 = 1;
            } else if (S[i] == '1') {
                f0 = 1;
                f1 = 0
            }
        } else {
            if (S[i] == '0') {
                f0 = g0
                f1 = Math.min(g1 + 1, g0 + 1)
            } else {
                f0 = g0 + 1
                f1 = Math.min(g0, g1)
            }
        }
        g0 = f0
        g1 = f1
        // console.log(f0,f1)
    }
    return Math.min(f0, f1)
};