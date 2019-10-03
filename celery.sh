<<<<<<< HEAD

  
celery -A config worker -c 5 --loglevel=info -Q b2c_result,c2b_confirmation,c2b_validation,online_checkout_request,online_checkout_callback
=======
celery -A config worker -c 5 --loglevel=info -Q b2c_result,c2b_confirmation,c2b_validation,online_checkout_request,online_checkout_callback
>>>>>>> 555a810b9e5b10dfa11c1477238b0adeaf84a3f7
