
it('test', () => {
cy.visit("http://google.com")

cy.get('[href="https://store.google.com/CA?utm_source=hp_header&utm_medium=google_ooo&utm_campaign=GS100042&hl=en-CA"]').click()

cy.url().should('include', 'https://store.google.com/CA/?utm_source=hp_header&utm_medium=google_ooo&utm_campaign=GS100042&hl=en-CA')

cy.get('.hamburger > svg > path').click()

cy.get('button[data-category-id="phones"] > .cat-image').click()

cy.get('[style="height: 496px;"] > :nth-child(1) > .subcategory-links > .shop-all').click()

cy.get('#meet-pixel-4 > .mqn2-aaz > .mqn2-ab0 > .mqn2-ab1 > .mqn2-af3 > .mqn2-af4 > .mqn2-af6 > :nth-child(1) > .mqn2-aal').click()


})