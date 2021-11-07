function hideBlock(blockId,message)
{
    
    document.getElementById(blockId).style.display = "none";
    if(message !== "")
    {
        setTimeout(function(){alert(message);console.log("heyy")},1000);
    }

}


function signup()
{
    document.getElementById('login').style.display = "none";
    document.getElementById('signup').style.display = "flex";
}

function login()
{
    document.getElementById('login').style.display = "flex";
    document.getElementById('signup').style.display = "none";
}


function showTagScreen(isTag,tagName)
{
    if(isTag)
    {
        console.log(tagName)
    }
    document.getElementById('updateTagsBlock').style.display = "none";
    document.getElementById('TagListBlock').style.display = "block";

}


function formManipulate(name)
{
    console.log(name)
}