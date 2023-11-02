$(document).ready(() => {
    $("#loginForm").validate({
        rules: {
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
          username: {
            required: "Поле 'Имя пользователя' обязательно для заполнения.",
            maxlength: "Имя не должно содержать более 50 символов."
          },
          password: {
            required: "Поле 'Пароль' обязательно для заполнения.",
            maxlength: "Пароль не должен содержать более 50 символов."
          },

        },
        errorPlacement: function(error, element) {
            error.insertAfter(element);
        }
    });

})