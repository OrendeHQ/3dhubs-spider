#!/bin/bash
echo "{\"data\": [" > data.json
for i in {0..6}
do
    echo -c '{"requests":[{"indexName":"Production Printers","params":"query=&page='"$i"'&facets=%5B%22price%22%2C%22type%22%2C%22category%22%2C%22level%22%2C%22connectivity%22%2C%22show_on_index%22%2C%22volume_depth%22%2C%22volume_height%22%2C%22volume_width%22%5D&tagFilters=&facetFilters=%5B%5B%22show_on_index%3Atrue%22%5D%5D"},{"indexName":"Production Printers","params":"query=&page=0&hitsPerPage=1&attributesToRetrieve=%5B%5D&attributesToHighlight=%5B%5D&attributesToSnippet=%5B%5D&tagFilters=&facets=show_on_index"}]}'
    curl -H "Content-Type: application/json" \
    -X POST \
    -d '{"requests":[{"indexName":"Production Printers","params":"query=&page='"$i"'&facets=%5B%22price%22%2C%22type%22%2C%22category%22%2C%22level%22%2C%22connectivity%22%2C%22show_on_index%22%2C%22volume_depth%22%2C%22volume_height%22%2C%22volume_width%22%5D&tagFilters=&facetFilters=%5B%5B%22show_on_index%3Atrue%22%5D%5D"},{"indexName":"Production Printers","params":"query=&page=0&hitsPerPage=1&attributesToRetrieve=%5B%5D&attributesToHighlight=%5B%5D&attributesToSnippet=%5B%5D&tagFilters=&facets=show_on_index"}]}' \
    "https://9pkjx8rw07-dsn.algolia.net/1/indexes/*/queries?x-algolia-agent=Algolia%20for%20AngularJS%203.18.0%3BJS%20Helper%202.21.0&x-algolia-application-id=9PKJX8RW07&x-algolia-api-key=041f64fe2cf5b838caab8e504f7a75a7" \
    | jq -r ".results[0].hits" \
    >> data.json
    echo ',' >> data.json
done
echo "] }" >> data.json