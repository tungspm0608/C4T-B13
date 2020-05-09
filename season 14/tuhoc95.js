var diem = 0;
var vitrimaudung
function taomau() {
    var r = Math.floor(Math.random()*255);
    var g = Math.floor(Math.random()*255);
    var b = Math.floor(Math.random()*255);
    var maudung = `rgb(${r},${g},${b})`;
    var laymaudung = document.getElementById('somaungaunhien');
    laymaudung.textContent = maudung;
    var tatcabong = document.getElementById('tatcabong');
    var bong1 = tatcabong.getElementsByClassName('bong');
    vitrimaudung = Math.floor(Math.random() * 3);
    bong1[vitrimaudung].style.backgroundColor = maudung;
    for(i = 0; i < bong1.length ; i++) {
        if (i != vitrimaudung) {
            var soloi = Math.random() * 100 - 50;
            var x = Math.random();
            if (x < 0,5) {soloi = - soloi}
            else{soloi = soloi};
            var mauloi = `rgb(${r + soloi},${g + soloi},${b + soloi})`;
        bong1[i].style.backgroundColor = mauloi;
        }
    console.log(vitrimaudung + 1)    
    };
}
function doan() {
    var tatcabong = document.getElementById('tatcabong');
    var bong1 = tatcabong.getElementsByClassName('bong');
    for (i = 0;i < bong1.length; i ++ ) {    
        bong1[i].addEventListener("click",function(e) {
        var bong = e.target;
        var vitricuabong = bong.getAttribute("index");
        if (vitricuabong == vitrimaudung) {
            diem += 1
        }else{
            diem = 0
        };
        var tongdiem = document.getElementById('diem');
        tongdiem.textContent = `diem: ${diem}`;
        taomau()
        })
    };    
};
taomau();
doan();
