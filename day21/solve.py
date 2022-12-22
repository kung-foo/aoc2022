#!/usr/bin/env python3
from sympy import solve, symbols, Eq

prqz = symbols('prqz')
hgsf = symbols('hgsf')
hddd = symbols('hddd')
gplf = symbols('gplf')
qqlp = symbols('qqlp')
zvqf = symbols('zvqf')
tbwf = symbols('tbwf')
pgnl = symbols('pgnl')
wpdb = symbols('wpdb')
ggbd = symbols('ggbd')
tlzl = symbols('tlzl')
znbf = symbols('znbf')
flpm = symbols('flpm')
cqlp = symbols('cqlp')
qcjn = symbols('qcjn')
szrj = symbols('szrj')
rdhb = symbols('rdhb')
clph = symbols('clph')
jlmn = symbols('jlmn')
lllg = symbols('lllg')
rfpm = symbols('rfpm')
jqqp = symbols('jqqp')
rqmd = symbols('rqmd')
fbmd = symbols('fbmd')
vmfb = symbols('vmfb')
pgpd = symbols('pgpd')
lsbv = symbols('lsbv')
cmlb = symbols('cmlb')
hwjr = symbols('hwjr')
nvzq = symbols('nvzq')
mfwf = symbols('mfwf')
zlww = symbols('zlww')
zhhs = symbols('zhhs')
cnnm = symbols('cnnm')
zssb = symbols('zssb')
fmqr = symbols('fmqr')
tbrs = symbols('tbrs')
rcvf = symbols('rcvf')
jfql = symbols('jfql')
zfvm = symbols('zfvm')
sgrv = symbols('sgrv')
tvjc = symbols('tvjc')
rtlm = symbols('rtlm')
rhlj = symbols('rhlj')
crws = symbols('crws')
dqcw = symbols('dqcw')
lvcj = symbols('lvcj')
lscn = symbols('lscn')
frmf = symbols('frmf')
pdvm = symbols('pdvm')
fcvb = symbols('fcvb')
ctnl = symbols('ctnl')
rzbr = symbols('rzbr')
vcvh = symbols('vcvh')
jvcn = symbols('jvcn')
vnms = symbols('vnms')
root = symbols('root')
rgnl = symbols('rgnl')
ddbt = symbols('ddbt')
vwmb = symbols('vwmb')
nqjf = symbols('nqjf')
humn = symbols('humn')
lcdq = symbols('lcdq')
phcp = symbols('phcp')
mthr = symbols('mthr')
mchh = symbols('mchh')
lgdf = symbols('lgdf')
cntw = symbols('cntw')
srqz = symbols('srqz')
gvph = symbols('gvph')

f = [
    Eq(prqz, 471 + gplf),
    Eq(hgsf, 206 + jvcn),
    Eq(hddd, srqz / 8),
    Eq(gplf, 9 * jqqp),
    Eq(qqlp, tvjc - 138),
    Eq(zvqf, zhhs - 174),
    Eq(tbwf, zvqf * 2),
    Eq(pgnl, hddd - 869),
    Eq(wpdb, 824 + fcvb),
    Eq(ggbd, dqcw - 307),
    Eq(tlzl, rzbr - 929),
    Eq(znbf, 2 * tbrs),
    Eq(flpm, 217 + tlzl),
    Eq(cqlp, cntw * 2),
    Eq(qcjn, ggbd / 7),
    Eq(szrj, 647 + humn),
    Eq(rdhb, 45 + zfvm),
    Eq(clph, znbf - 735),
    Eq(jlmn, 33 * qqlp),
    Eq(lllg, 2 * pgnl),
    Eq(rfpm, 2 * lgdf),
    Eq(jqqp, fmqr - 322),
    Eq(rqmd, rhlj - 382),
    Eq(fbmd, flpm / 2),
    Eq(vmfb, 384 + tbwf),
    Eq(pgpd, hwjr - 722),
    Eq(lsbv, 2 * lvcj),
    Eq(cmlb, 556 + lllg),
    Eq(hwjr, szrj / 3),
    Eq(nvzq, 680 + clph),
    Eq(mfwf, lscn - 180),
    Eq(zlww, sgrv * 6),
    Eq(zhhs, frmf * 3),
    Eq(cnnm, rcvf - 436),
    Eq(zssb, crws - 698),
    Eq(fmqr, zssb * 2),
    Eq(tbrs, zlww + 634),
    Eq(rcvf, jfql / 2),
    Eq(jfql, nvzq + 313),
    Eq(zfvm, cmlb / 2),
    Eq(sgrv, 628 + qcjn),
    Eq(tvjc, wpdb / 7),
    Eq(rtlm, vmfb / 5),
    Eq(rhlj, prqz / 7),
    Eq(crws, rdhb / 7),
    Eq(dqcw, ctnl * 9),
    Eq(lvcj, 18251426596821 - vcvh),
    Eq(lscn, 2 * mthr),
    Eq(frmf, 566 + vwmb),
    Eq(pdvm, 957 + phcp),
    Eq(fcvb, rgnl / 2),
    Eq(ctnl, 337 + fbmd),
    Eq(rzbr, vnms / 7),
    Eq(vcvh, pdvm / 2),
    Eq(jvcn, jlmn - 578),
    Eq(vnms, gvph + 200),
    Eq(lsbv, 2228768553328),
    Eq(rgnl, 606 + ddbt),
    Eq(ddbt, 4 * rqmd),
    Eq(vwmb, cnnm / 3),
    Eq(nqjf, cqlp - 825),
    Eq(lcdq, hgsf / 3),
    Eq(phcp, mfwf / 2),
    Eq(mthr, 821 + rtlm),
    Eq(mchh, 105 * pgpd),
    Eq(lgdf, 712 + mchh),
    Eq(cntw, 746 + lcdq),
    Eq(srqz, rfpm - 570),
    Eq(gvph, nqjf * 2),
]

print("part2", solve(f)[humn])
