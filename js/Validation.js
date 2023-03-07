function myf(e)
{
	var c=((e.which>=65 && e.which<91)||(e.which==8))
	{
		document.getElementById("error").style.display=c?"none":"inline"
	}
	return c;
}
    let isNumber = (evt) => {
        let iKeyCode = (evt.which) ? evt.which : evt.keyCode
        if (iKeyCode != 46 && iKeyCode > 31 && (iKeyCode < 48 || iKeyCode > 57))
            return false;
        
        return true;
        
    }

