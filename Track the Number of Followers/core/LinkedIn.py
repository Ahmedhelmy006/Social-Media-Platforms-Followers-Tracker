#To preven spaghetti code, I creaated a module to keep all my LinkedIn Selectors

class NormalPageView:
    number_of_followers_class = "t-14 t-normal text-align-center"

class ProfileView:
    number_of_followers_class = "text-body-small t-black--light inline-block"

class Newsteller:
    number_of_subscribers_selector = (
        'div.display-flex.align-items-baseline.flex-column.justify-center '
        'p[data-test-publishing-subscribers-text="true"]'
    )
