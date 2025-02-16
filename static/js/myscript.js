/**
 * When the DOMContent is loaded, it will trigger a function.
 * An eventlistener will listen for the radio buttons to be clicked.
 */

const editButton = document.getElementsByClassName("btn-edit")
const commentText = document.getElementsByClassName("edit_text")
const commentForm = document.getElementById("menuForm")
const submitButton = document.getElementsByClassName("submitButton")


for (let button of editButton) {
    button.addEventListener("click", (e) => {
     let menuId = e.target.getAttribute("menu_id");       
     let feedbackContent = document.getElementById("comment").innerText;
     commentText.value = feedbackContent;   
     submitButton.innerText = "Update";
     commentForm.setAttribute("action", ``);
     });
}
