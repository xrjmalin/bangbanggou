function $(id){
	return typeof id==='string'?document.getElementById(id):id;
}
window.onload=function(){
	var titles=$('title-con').getElementsByTagName('li');
	var   divs=$('market-con').getElementsByClassName('market-content');
	if(titles.length!=divs.length)
		return;
	for(var i=0;i<titles.length;i++)
	{
		titles[i].id=i;
		titles[i].onclick=function()
		{
			for(var j=0;j<titles.length;j++)
			{
				titles[j].className='';
                divs[j].style.display='none';
			}
			this.className='select';
			divs[this.id].style.display='block';
		}
	}
}
function showmenu(li){
	var submenus=li.getElementsByTagName('ul')[0];
	submenus.style.display='block';
}

function hidemenu(li){
	var hide=li.getElementsByTagName('ul')[0];
	hide.style.display='none';
}
