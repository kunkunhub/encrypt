var s = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~";

function ch(x) {
    return s.charAt(x % s.length);
}
function od(c) {
    return s.indexOf(c);
}

function encrypt(key, m) {
    var tmp = key;
    while (key.length < m.length) {
        key = key + tmp;
    }

    ans = "";
    for (var i = 0; i < m.length; i++) {
        ans += ch(od(m[i]) + od(key[i]) + i);
    }
    return ans;
}
function decrypt(key, m) {
    tmp = key;
    while (key.length < m.length) {
        key = key + tmp;
    }
    ans = "";
    for (var i = 0; i < m.length; i++) {
        ans += ch(od(m[i]) - od(key[i]) - i);
    }
    return ans;
}

function m() {
    var input = document.getElementById('input');
    var something = document.getElementById('something');
    something.innerHTML = "<div id='something'>" + (encrypt("abc", input.value)) + "</div>";
}