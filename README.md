# gateway-template
Billing gateway template for Fleio.

* Copy the "newgateway" folder from the repository and add it in the `/var/webapps/fleio/project/fleio/billing/gateways/` location
* Add the following line of code in your settings.py file:
```python
INSTALLED_APPS += ('fleio.billing.gateways.newgateway', )
```
* Restart the django server and you should be able to see the new gateway in Fleio frontend on the staff/billing/gateways page
