$(function () {
    //enable disable button for search form
    let search_button=$('#search-button');
    let search_text=$('#search-text');
    search_text.keyup((e)=>{
      if (search_text.val().trim()==''){
        search_button.prop('disabled',true);
      }
      else {
        search_button.prop('disabled',false);
      }
    });
});