import { timeout } from "async"

it('test', () => {

    cy.server().route("POST", '**/v1/stats').as('testdata')
    cy.visit("https://www.twitch.tv")

    // cy.wait(3000)
    cy.wait('@testdata').its('status').should('be', 200)
    cy.get('.carousel-player-nav-arrow__container.tw-right-0 > .tw-flex > .tw-align-middle').click()
})

