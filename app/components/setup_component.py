from app.services.setup_service import from_bfm_get_setup, from_bfm_post_setup


def process_get_setup():
    response = from_bfm_get_setup()
    return response


def process_post_setup(setup):
    response = from_bfm_post_setup(setup)
    return response
