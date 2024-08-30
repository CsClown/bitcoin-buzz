const editButtons = document.getElementsByClassName("btn-edit");
const replyFormContainer = document.getElementById("reply-form-container");
const replyForm = document.getElementById("replyForm");
const replyText = document.getElementById("id_content");  // Assuming 'id_content' is the ID for the reply content textarea
const replyIdInput = document.getElementById("reply_id_input");
const submitButton = document.getElementById("submitButton");
const formTitle = document.getElementById("form-title");
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteConfirm = document.getElementById("deleteConfirm");

for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        let replyId = e.target.getAttribute("data-reply_id");
        let replyContent = document.getElementById(`reply${replyId}`).innerText;

        // Populate the form with the reply content and ID
        replyText.value = replyContent;
        replyIdInput.value = replyId;

        // Update the form title and submit button text
        formTitle.textContent = "Edit your reply:";
        submitButton.innerText = "Update";

        // Show the reply form
        replyFormContainer.style.display = "block";
        
        document.getElementById("reply-form-container").scrollIntoView({
            behavior: 'smooth', // This makes the scrolling smooth
            block: 'start'      // This aligns the element to the top of the view
        });
    });
}

document.getElementById("show-reply-form").addEventListener("click", function () {
    // Reset the form for creating a new reply
    replyForm.reset();
    replyIdInput.value = "";
    formTitle.textContent = "Post a reply:";
    submitButton.innerText = "Submit";
    
    replyFormContainer.style.display = "block";
});



/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific item
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/


  for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let replyId = e.target.getAttribute("data-reply_id");
        let postId = e.target.getAttribute("data-post_id");

        if (replyId) {
            deleteConfirm.href = `delete_reply/${replyId}`;
        } else if (postId) {
            deleteConfirm.href = `delete_post/${postId}`;
        }

        deleteModal.show();
    });
}

