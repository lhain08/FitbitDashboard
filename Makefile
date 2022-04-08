fmt:
	autoflake -i -r --expand-star-imports --remove-all-unused-imports --ignore-init-module-imports --remove-unused-variables . --exclude __init__ \
	&& autopep8 -i -r --exclude __init__.py . \
	&& black .

lint:
	autoflake -c -r --expand-star-imports --remove-all-unused-imports --ignore-init-module-imports --remove-unused-variables . --exclude __init__ \
	&& black . --check \