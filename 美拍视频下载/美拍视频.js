
////////////
var Cryoptojs = require('crypto-js');

var h = "substring"
    , i = "split"
    , j = "replace"
    , k = "substr";

decodeMp4 = {
    getHex: function (a) {
        return {
            str: a[h](4),
            hex: a[h](0, 4)[i]("").reverse().join("")
        }
    },
    getDec: function (a) {
        var b = parseInt(a, 16).toString();
        return {
            pre: b[h](0, 2)[i](""),
            tail: b[h](2)[i]("")
        }
    },
    substr: function (a, b) {
        var c = a[h](0, b[0])
            , d = a[k](b[0], b[1]);
        return c + a[h](b[0])[j](d, "")
    },
    getPos: function (a, b) {
        return b[0] = a.length - b[0] - b[1],
            b
    },
    decode: function (a) {
        var b = this.getHex(a)
            , c = this.getDec(b.hex)
            , d = this[k](b.str, c.pre);
        var parsedWordArray = Cryoptojs.enc.Base64.parse(this[k](d, this.getPos(d, c.tail)));
        return parsedWordArray.toString(Cryoptojs.enc.Utf8);
    }
};
t = '4941Ly9td7ynZpZGVvMTAubWVpdHVkYXRhLmNvbS81ZGRjYTA5YWVkMjAySDI2NFdFQjI3NTgxN19IMjY0X01QNWRkY2E3LmgpmTPi2k1wNA==';

console.log(decodeMp4.decode(t));




