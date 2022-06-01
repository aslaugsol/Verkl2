function getvalues()
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
    };
