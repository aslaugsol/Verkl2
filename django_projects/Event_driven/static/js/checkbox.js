/*function getvalues()
    {
        var selected=new Array();
        var chkbox = document.getElementById("tab1");
        var selchk=chkbox.getElementsByTagName("input");
        for(var i=0;i<selchk.length;i++)
        {
            if(selchk[i].checked)
            {
                selected.push(selchk[i].value);
            }
        }
        if(selected.length>0)
        {
            document.getElementById("displayvalues").innerHTML=selected;
        }
    };*/

function getvalues() {
    var selected = document.querySelector('input[name="category"]:checked');
    console.log(":)");
    var catId = selected.attributes.datacategory.value;
    console.log(catId);
    console.log(":)");
    return catId;
}

getvalues();