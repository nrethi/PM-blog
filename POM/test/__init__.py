- name: Set up
  run: |
    mkdir test
    echo "print('OK')" > test/a.py
    touch test/__init__.py