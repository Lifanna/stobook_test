$(document).ready(() => {
    $(".phone_number").inputmask("+7(999)-999-99-99");
    $("#registerForm").validate({
        rules: {
            first_name: {
                required: true,
                maxlength: 50
            },
            last_name: {
                required: true,
                maxlength: 50
            },
            date_of_birth: {
                required: true,
            },
            email: {
                required: true,
                maxlength: 50
            },
            username: {
                required: true,
                maxlength: 50
            },
            password: {
                required: true,
                maxlength: 50
            },
        },
        messages: {
          first_name: {
            required: "Поле 'Имя' обязательно для заполнения.",
            maxlength: "Имя не должно содержать более 50 символов."
          },

        },
        errorPlacement: function(error, element) {
            error.insertAfter(element);
        }
    });

    $("#registerForm").submit(function(event) {
        if ($("#registerForm").valid()) {
          // Форма валидна, можно выполнять действия
          alert("Форма валидна. Данные могут быть отправлены.");
        } else {
          // Форма недействительна, предотвращаем отправку
          event.preventDefault();
        }
    });
})
