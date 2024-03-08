

def fill_username(model) -> None:
    from hiddifypanel import hutils
    if model.username:
        return
    base_username = model.name or ''
    minimum_username_length = 10

    if len(base_username) < minimum_username_length:
        base_username += hutils.random.get_random_string(minimum_username_length - len(base_username), minimum_username_length)

    if len(base_username) > 100:
        base_username = base_username[0:100]
    model.username = base_username

    while not model.is_username_unique():
        rand_str = hutils.random.get_random_string(2, 4)
        model.username += rand_str


def fill_password(model) -> None:
    from hiddifypanel import hutils
    # TODO: hash the password
    if not model.password or len(model.password) < 16:
        model.password = hutils.random.get_random_password(length=16)
