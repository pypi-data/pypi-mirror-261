#!/usr/bin/env bash

if [[ ! "$CIRRUS_TAG" =~ ^refs/tags/v[0-9]+\.[0-9]+\.[0-9]+ ]]; then
  echo "Not a release. No need to deploy!"
  exit 0
fi

if [[ "$GITHUB_TOKEN" == "" ]]; then
  echo "Please provide GitHub access token via GITHUB_TOKEN environment variable!"
  exit 1
fi

if [[ "$TWINE_PASSWORD" == "" ]]; then
  echo "Please provide PyPI access token via TWINE_PASSWORD environment variable!"
  exit 1
fi

echo "Uploading $CIRRUS_TAG to GitHub release"

file_content_type="application/octet-stream"
files_to_upload=wheelhouse/*.whl
for fpath in $files_to_upload
do
  echo "Uploading $fpath..."
  name=$(basename "$fpath")
  url_to_upload="https://uploads.github.com/repos/$CIRRUS_REPO_FULL_NAME/releases/$CIRRUS_RELEASE/assets?name=$name"
  curl -X POST \
    --data-binary @$fpath \
    --header "Authorization: token $GITHUB_TOKEN" \
    --header "Content-Type: $file_content_type" \
    $url_to_upload
done

echo "Uploading $CIRRUS_TAG to PyPI"
pip install twine
twine upload $files_to_upload
