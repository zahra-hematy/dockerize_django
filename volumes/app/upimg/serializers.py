


class UserLoginSerializer(ModelSerializer):
    token = CharField(allow_blank=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'token',
        ]
        extra_kwargs = {"password":
                            {"write_only": True}
                        }

    def validate(self, data):
        user_obj = None
        username = data.get("username", None)
        password = data["password"]
        if not username:
            raise ValidationError("Kullanıcı adı gerekli.")

        user = User.objects.filter(
            Q(username=username)
            ).distinct()
        user = user.exclude(email__isnull=True).exclude(email__iexact='')
        if user.exists() and user.count() == 1:
            user = user.first()
        else:
            raise ValidationError("Böyle bir Kullanıcı Adı yoktur.")

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Tekrar deneyiniz.")
        data["token"] = "asdasdasdasd"
        return data