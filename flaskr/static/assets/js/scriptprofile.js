



var j;
var cont;
$('#addField').click(function() {
cont++;
$('#divLabel').append("<div class=\"container col\"><label for=\"uname\"><b><strong>Campo #"+cont+"</strong></b></label> <input id=\"field"+cont+"\" type=\"uname\" placeholder=\"Inserisci campo aggiuntivo\" name=\"campo"+cont+"\"required></div>");
});
$('#myButton').click( function() {
cont = 1;
document.getElementById('id01').style.display='block';
document.getElementById('addField').style.display='block';  
$('#form1').attr('action','/create_proj');
$('#divLabel').html("");
$('#divLabel').append("<div class=\"container col\"><label for=\"uname\"><b><strong>Nome Progetto</strong></b></label><input type=\"text\" placeholder=\"nome\" name=\"nome\" required></div>");
$('#divLabel').append("<div class=\"container col\"><label for=\"uname\"><b><strong>Descrizione</strong></b></label><input type=\"text\" placeholder=\"inserisci Descrizione\" name=\"desc\" required></div>");
$('#divLabel').append("<div class=\"container col\"><label for=\"uname\"><b><strong>Anno scadenza</strong></b></label><input id=\"anno\" type=\"number\"placeholder=\"Inserisci anno\" name=\"anno_scadenza\" required></div>");
$('#divLabel').append("<div class=\"container col\"><label for=\"uname\"><b><strong>Mese scadenza</strong></b></label><input id=\"mese\" type=\"number\" min=\"1\" max=\"12\"placeholder=\"Inserisci mese\" name=\"mese_scadenza\" required></div>");
$('#divLabel').append("<div class=\"container col\"><label for=\"uname\"><b><strong>Giorno scadenza</strong></b></label><input id=\"giorno\" type=\"number\"min=\"1\" max=\"31\" placeholder=\"Inserisci giorno\" name=\"giorno_scadenza\" required></div>");
$('#divLabel').append("<div class=\"container col\"><label for=\"uname\"><b><strong>Campo #1</strong></b></label><input id=\"field"+cont+"\" type=\"text\" placeholder=\"Inserisci Campo\" name=\"campo1\" required></div></div>");

});




$('#invia').click(function checkField()
{

	var field;
	var field2;
	for(var i=1; i<cont; i++)
	{
		field = document.getElementById('field'+i.toString()).value;
		for(var j=i+1; j<=cont; j++)
		{
			field2= document.getElementById('field'+j.toString()).value;
			if(field == field2)
			{
				alert("Hai inserito due Campi con lo stesso valore");
	          		document.getElementById('id01').style.display = 'none';
				return false;
			}
		}		
	}

var    y = document.getElementById('anno').value;
var    m = document.getElementById('mese').value;
var    d = document.getElementById('giorno').value;
var    da = new Date();
var    yt = da.getFullYear();
var    mt = da.getMonth();
var    dt = da.getDate();
var    newdate = new Date(yt, mt-1, dt);
var daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31];


if((!(y % 4) && y % 100) || !(y % 400)){
    daysInMonth[1] = 29;
}

if(!(/\D/.test(String(d))) && d > 0 && d<= daysInMonth[--m])
{
    date = new Date(y, m-1, d);
    if(date > newdate)
    {
        return true;
    }
    else
    {
        alert('Data Non Valida');
        return false;
    }
}
else {

    return false;
}


});
