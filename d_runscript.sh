#/bin/bash
cd /home/sumonta/Django/django_local_library
source ../../Django/bin/activate

output=$(ps -ef | grep "manage.py" | grep -v "grep"| awk '{print $2}' | head -n 1)
if [ -n "$output" ]; then
  echo "Running"
  echo "$output"
else
 echo "Not Running"
 python manage.py runserver 0.0.0.0:9192
fi
