var Cryoptojs = require('crypto-js');
const express = require('express');
const bodyParser = require('body-parser');
const app = express();
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));


app.post('/post',function (req,res) {

    data= req.body;
    console.log(
        "传过来的数值为: %s",data
    );
    function decrypt(href) {
        var s = "qnbyzzwmdgghmcnm";
        var hh = href;
        var aa = hh.split("/");
        var aaa = aa.length;
        var bbb = aa[aaa - 1].split('.');
        var ccc = bbb[0];
        var cccc = bbb[1];
        var r = /^\+?[1-9][0-9]*$/;
        if (r.test(ccc) && cccc.indexOf('jhtml') != -1) {
            var srcs = Cryoptojs.enc.Utf8.parse(ccc);
            var k = Cryoptojs.enc.Utf8.parse(s);
            var en = Cryoptojs.AES.encrypt(srcs, k, {
                mode: Cryoptojs.mode.ECB,
                padding: Cryoptojs.pad.Pkcs7
            });
            var ddd = en.toString();
            ddd = ddd.replace(/\//g, "^");
            ddd = ddd.substring(0, ddd.length - 2);
            var bbbb = ddd + '.' + bbb[1];
            aa[aaa - 1] = bbbb;
            var uuu = '';
            for (i = 0; i < aaa; i++) {
                uuu += aa[i] + '/'
            }
            uuu = uuu.substring(0, uuu.length - 1);
            // window.open(uuu)
            return uuu
        } else {
            var ee = $(this).attr('target');
            if (ee.typeof('undefined')) {
                // window.location = hh
                return uuu
            } else {
                // window.open(hh)
                return uuu
            }
        }

    }

    let datas = decrypt(data['href']);
    console.log(
        '返回的参数为:%s',datas
    );
    res.json(datas)
});

const server = app.listen(8000, function () {
    let port = server.address().port;
    console.log(
        "node服务启动，监听地址为: http://%s:%s", '127.0.0.1', port
    )
});