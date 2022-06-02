import configparser
config = configparser.RawConfigParser()
config.read(filenames="../config.properties")

email_provider_smtp_address = config.get("email-info", "email_smtp")
email_port = config.get("email-info", "email_port")
email_sender = config.get("email-info", "email_account")
email_password = config.get("email-info", "email_password")

