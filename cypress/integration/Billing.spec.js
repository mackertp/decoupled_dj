 context("Billing app", () => {
    describe("Invoice creation", () => {
        it("can create a new invoice", () => {
            cy.intercept("GET", "/billing/api/clients", {
                statusCode:200,
                body: [
                    {
                        id: 1,
                        name: "Juliana",
                        email: "juliana@acme.io",
                    },
                ],
            });
            cy.visit("http://localhost:8080/");
            cy.get("form").within(() => {
                cy.get("select").select(
                    "Juliana - juliana@acme.io"
                );
            });
        });
    });
});