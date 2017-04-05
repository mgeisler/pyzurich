#[macro_use]
extern crate serde_derive;
extern crate serde_json;
extern crate hyper;
extern crate chrono;

use hyper::client::Client;
use chrono::{UTC, TimeZone};

#[derive(Deserialize, Debug)]
struct Event {
    name: String,
    time: i64,
    yes_rsvp_count: u16,
    venue: Venue,
}

#[derive(Deserialize, Debug)]
struct Venue {
    name: String,
    address_1: String,
    city: String,
    country: String,
}


fn main() {
    let client = Client::new();
    let req = client.get("http://api.meetup.com/pyzurich/events/236240899");

    println!("Hello PyZurich!  Please wait, fetching data...");
    match req.send() {
        Ok(resp) => {
            println!("Response status: {}", resp.status);
            let event: Event = serde_json::from_reader(resp)
                .expect("Could not parse response!");
            println!("It is shortly after {} and '{}' will begin.",
                     UTC.timestamp(event.time / 1000, 0),
                     event.name);
            println!("Many thanks to all {} of you for coming to {}!",
                     event.yes_rsvp_count,
                     event.venue.address_1);
        }
        Err(err) => println!("Ups, an error occured: {}", err),
    }
}
