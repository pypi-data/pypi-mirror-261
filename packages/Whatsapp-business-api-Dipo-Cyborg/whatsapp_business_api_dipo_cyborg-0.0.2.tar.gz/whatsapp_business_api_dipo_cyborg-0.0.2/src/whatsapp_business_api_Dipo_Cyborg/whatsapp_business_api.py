import requests
import json
host = "https://graph.facebook.com"


class WhatsAppBusinessAPI:
    def __init__(self, from_number_id, api_key):
        self.api_key = api_key
        self.from_number_id = from_number_id

    def send_text_message(self, phone_number=None, message=None, context_id=None):
        url = f"{host}/v19.0/{self.from_number_id}/messages"

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": phone_number,
            "type": "text",
            "text": {
                "preview_url": False,
                "body": message
            }
        }
        if (context_id):
            data.update({"context": {"message_id": context_id}})
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        data = json.dumps(data)

        response = requests.post(url, data=data, headers=headers)
        status_code = response.status_code
        data = response.json()
        print(data)
        data = {"status_code": status_code, "data": data,
                "to": data['contacts'][0]['input'], "to_id": data['contacts'][0]['wa_id'], "message_id": data['messages'][0]['id']}
        return data

    def send_text_message_with_url(self, phone_number=None, message=None, url=None, context_id=None):
        url_ = f"{host}/v19.0/{self.from_number_id}/messages"

        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": phone_number,
            "type": "text",
            "text": {
                "preview_url": True,
                "body": message,
                "customizations": {
                    "link": {
                        "url": url
                    }
                }
            }
        }

        if (context_id):
            data.update({"context": {"message_id": context_id}})

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        data = json.dumps(data)

        response = requests.post(url_, data=data, headers=headers)
        status_code = response.status_code
        data = response.json()
        data = {"status_code": status_code, "data": data,
                "to": data['contacts'][0]['input'], "to_id": data['contacts'][0]['wa_id'], "message_id": data['messages'][0]['id']}
        return data

    def send_media_message(self, phone_number=None, document_url=None, caption=None, type="image", context_id=None):
        """
        type: image|video|document|audio|sticker
        """
        url = f"{host}/v19.0/{self.from_number_id}/messages"
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": phone_number,
            "type": type,
        }
        data.update({
            f"{type}": {
                "url": document_url,
                "caption": caption
            }
        })

        if (context_id):
            data.update({"context": {"message_id": context_id}})

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        data = json.dumps(data)

        response = requests.post(url, data=data, headers=headers)
        status_code = response.status_code
        data = response.json()
        data = {"status_code": status_code, "data": data,
                "to": data['contacts'][0]['input'], "to_id": data['contacts'][0]['wa_id'], "message_id": data['messages'][0]['id']}
        return data

    def send_location_message(self, phone_number=None, latitude=None, longitude=None, name=None, address=None, context_id=None):
        url = f"{host}/v19.0/{self.from_number_id}/messages"
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": phone_number,
            "type": "location",
            "location": {
                "latitude": latitude,
                "longitude": longitude,
                "name": name,
                "address": address
            }
        }

        if (context_id):
            data.update({"context": {"message_id": context_id}})

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        data = json.dumps(data)

        response = requests.post(url, data=data, headers=headers)
        status_code = response.status_code
        data = response.json()
        data = {"status_code": status_code, "data": data,
                "to": data['contacts'][0]['input'], "to_id": data['contacts'][0]['wa_id'], "message_id": data['messages'][0]['id']}
        return data

    def send_contact_message(self, phone_number=None, contacts=[], context_id=None):
        __doc__ = """
        contacts looks somewhat like this;
         "contacts": [{
      "addresses": [{
          "street": "STREET",
          "city": "CITY",
          "state": "STATE",
          "zip": "ZIP",
          "country": "COUNTRY",
          "country_code": "COUNTRY_CODE",
          "type": "HOME"
        },
        {
          "street": "STREET",
          "city": "CITY",
          "state": "STATE",
          "zip": "ZIP",
          "country": "COUNTRY",
          "country_code": "COUNTRY_CODE",
          "type": "WORK"
        }],
      "birthday": "YEAR_MONTH_DAY",
      "emails": [{
          "email": "EMAIL",
          "type": "WORK"
        },
        {
          "email": "EMAIL",
          "type": "HOME"
        }],
      "name": {
        "formatted_name": "NAME",
        "first_name": "FIRST_NAME",
        "last_name": "LAST_NAME",
        "middle_name": "MIDDLE_NAME",
        "suffix": "SUFFIX",
        "prefix": "PREFIX"
      },
      "org": {
        "company": "COMPANY",
        "department": "DEPARTMENT",
        "title": "TITLE"
      },
      "phones": [{
          "phone": "PHONE_NUMBER",
          "type": "HOME"
        },
        {
          "phone": "PHONE_NUMBER",
          "type": "WORK",
          "wa_id": "PHONE_OR_WA_ID"
        }],
      "urls": [{
          "url": "URL",
          "type": "WORK"
        },
        {
          "url": "URL",
          "type": "HOME"
        }]
    }]
        """
        url = f"{host}/v19.0/{self.from_number_id}/messages"
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": phone_number,
            "type": "contacts",
            "contacts": contacts
        }

        if (context_id):
            data.update({"context": {"message_id": context_id}})

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        data = json.dumps(data)

        response = requests.post(url, data=data, headers=headers)
        status_code = response.status_code
        data = response.json()
        data = {"status_code": status_code, "data": data,
                "to": data['contacts'][0]['input'], "to_id": data['contacts'][0]['wa_id'], "message_id": data['messages'][0]['id']}
        return data

    def send_template_message(self, phone_number=None, template_name=None, language_code="en_GB", header_image=None, context_id=None):
        __doc__ = """
        """
        url = f"{host}/v19.0/{self.from_number_id}/messages"
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": phone_number,
            "type": "template",
            "template": {
                "name": template_name,
                "language": {
                    "code": language_code
                },
            }
        }
        data.update({"components": [{
            "type": "body",
            "parameters": [
                {
                    "type": "text",
                    "text": "text-string"
                },
            ]
        }
        ]})
        if (header_image != None):
            data.componenets.push({
                "type": "header",
                "parameters": [
                    {
                        "type": "image",
                        "image": {
                            "link": header_image
                        }
                    }
                ]
            })

        if (context_id):
            data.update({"context": {"message_id": context_id}})

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        data = json.dumps(data)

        response = requests.post(url, data=data, headers=headers)
        status_code = response.status_code
        data = response.json()
        data = {"status_code": status_code, "data": data,
                "to": data['contacts'][0]['input'], "to_id": data['contacts'][0]['wa_id'], "message_id": data['messages'][0]['id']}
        return data

    def send_interactive_template(self, phone_number=None, template_name=None, language_code="en_GB", header_image=None, context_id=None):
        __doc__ = """
        localizable_params looks somewhat like this;
        "localizable_params": [
            {
              "default": "default",
              "currency": "USD",
              "amount": "100"
            }
          ]
        """
        url = f"{host}/v19.0/{self.from_number_id}/messages"
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": phone_number,
            "type": "interactive_template",
            "template": {
                "name": template_name,
                "language": {
                    "code": language_code
                },
            }
        }
        data.update({"components": [{
            "type": "body",
            "parameters": [
                {
                    "type": "text",
                    "text": "text-string"
                },
            ]
        }
        ]})
        if (header_image != None):
            data.componenets.push({
                "type": "header",
                "parameters": [
                    {
                        "type": "image",
                        "image": {
                            "link": header_image
                        }
                    }
                ]
            })

        if (context_id):
            data.update({"context": {"message_id": context_id}})

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        data = json.dumps(data)

        response = requests.post(url, data=data, headers=headers)
        status_code = response.status_code
        data = response.json()
        data = {"status_code": status_code, "data": data,
                "to": data['contacts'][0]['input'], "to_id": data['contacts'][0]['wa_id'], "message_id": data['messages'][0]['id']}
        return data

    def send_interactive_template_message(self, phone_number=None, template_name=None, language_code="en_GB", header_image=None, context_id=None, btns={}):
        __doc__ = """
        btns looks somewhat like this;
         {
        "type": "button",
        "sub_type": "quick_reply",
        "index": "0",
        "parameters": [
          {
            "type": "payload",
            "payload": "PAYLOAD"
          }
        ]
      }
      """
        url = f"{host}/v19.0/{self.from_number_id}/messages"
        data = {
            "messaging_product": "whatsapp",
            "recipient_type": "individual",
            "to": phone_number,
            "type": "interactive_template",
            "template": {
                "name": template_name,
                "language": {
                    "code": language_code
                },
            }
        }
        data.update({"components": [{
            "type": "body",
            "parameters": [
                {
                    "type": "text",
                    "text": "text-string"
                },
            ]
        }
        ]})
        if (header_image != None):
            data.componenets.push({
                "type": "header",
                "parameters": [
                    {
                        "type": "image",
                        "image": {
                            "link": header_image
                        }
                    }
                ]
            })

        data.update({"buttons": btns})

        if (context_id):
            data.update({"context": {"message_id": context_id}})

        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        data = json.dumps(data)

        response = requests.post(url, data=data, headers=headers)
        status_code = response.status_code
        data = response.json()
        data = {"status_code": status_code, "data": data,
                "to": data['contacts'][0]['input'], "to_id": data['contacts'][0]['wa_id'], "message_id": data['messages'][0]['id']}
        return data
