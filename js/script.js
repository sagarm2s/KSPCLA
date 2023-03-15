
    for (let i = 0; i < document.getElementsByClassName("dismissCrop").length; i++) {
        document.getElementsByClassName("dismissCrop")[i].addEventListener("click", function() {
            $("#cropmod_homepage").modal("hide");
            $("#employeeRegModal").modal("show");
        });
    }
    for (let i = 0; i < document.getElementsByClassName("closeEmployeeRegModal").length; i++) {
        document.getElementsByClassName("closeEmployeeRegModal")[i].addEventListener("click", function() {
            $("#addEmployeeEmploymentModal").modal("hide");
            $("#employeeAddModal").modal("show");
        });
    }
    