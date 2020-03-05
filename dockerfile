FROM cypress/included:4.1.0

COPY . /e2e

RUN npm install --save-dev mocha mochawesome mochawesome-merge mochawesome-report-generator

WORKDIR /e2e

ENV testtorun=""

ENTRYPOINT cypress run --reporter mochawesome --reporter-options "reportDir=results,overwrite=false,html=false,json=true" --spec "/e2e/cypress/integration/${testtorun}"