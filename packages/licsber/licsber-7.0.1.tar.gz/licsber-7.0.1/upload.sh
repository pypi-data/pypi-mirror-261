git pull

rm dist/*
python -m build
twine upload dist/*
