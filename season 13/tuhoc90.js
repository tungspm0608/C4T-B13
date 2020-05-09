var a = document.getElementById("song_container");
console.log(a)
var b = a.getElementsByClassName("song");
console.log(b)

for(var i = 0;i < b.length; i++ ){
    var c = b[i].getElementsByClassName('title')
    var d = b[i].getElementsByClassName('artist')

};
var deletet = a.getElementsByClassName('hello'); 
console.log(deletet)
for (var i = 0;i < deletet.length; i++) {
    var pop = deletet[i];
    pop.addEventListener('click',function(e){
        var btn = e.target;
        var div = btn.parentNode;
        div.remove(); 
    })
};
var edit = a.getElementsByClassName('hello1'); 
console.log(edit)
for (var i = 0;i < edit.length; i++) {
    var edits = edit[i];
    edits.addEventListener('click',function(r){
        var btn = r.target;
        var div = btn.parentNode;
        console.log(div)
    })
};
var more = a.getElementsByClassName('hello2'); 
console.log(more)
for (var i = 0;i < more.length; i++) {
    var mores = more[i];
    mores.addEventListener('click',function(t){
        var btn = t.target;
        var div = btn.parentNode;
        var c = div.getElementsByClassName('title')
        var d = div.getElementsByClassName('artist')
        console.log(c,d)
    })
};
function hello3() {
    console.log('<div> id = "song">..</div>')
}


