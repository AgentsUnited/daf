/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package tech.arg.toast.rest;

import org.restlet.Application;
import org.restlet.Component;
import org.restlet.Context;
import org.restlet.Restlet;
import org.restlet.data.Protocol;
import org.restlet.routing.Router;

/**
 * Main entrypoint for the TOAST argumentation engine
 * @author Mark Snaith
 */
public class Toast extends Application {

    /**
     * Main method
     * @param args 
     */
    public static void main(String[] args) {

        try {
            final Component component = new Component();
            component.getServers().add(Protocol.HTTP, 1234);

            Toast toast = new Toast(component.getContext().createChildContext());
            component.getDefaultHost().attach(toast);
            component.start();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    /**
     * Default constructor for the TOAST application
     * @param context 
     */
    public Toast(Context context) {
        super(context);
    }

    @Override
    public Restlet createInboundRoot() {

        Router router = new Router(getContext().createChildContext());
        router.attach("/evaluate", ToastResource.class);
        router.attach("/status", ToastResource.class);

        return router;

    }
}
