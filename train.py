import tkinter as tk
from tkinter import messagebox, StringVar, IntVar, ttk

def run():
    class TrainApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Train Ticket Booking")
            self.root.geometry("1540x810")
            self.root.config(bg="#ADD8E6")

            self.trains = {
                "Rajkot": {
                    "Ahmedabad": {
                        1: {
                            "name": "Gandhinagar Capital Intercity Express",
                            "timing": "12:55 AM - 5:02 AM",
                            "coaches": {
                                1: {"type": "General Coach", "ticket_price": 50}
                            }
                        },
                        2: {
                            "name": "Jablpur Somanth JBP EXP",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 840},
                                2: {"type": "Second Class", "ticket_price": 165},
                                3: {"type": "Sleeper", "ticket_price": 270},
                                4: {"type": "AC 2 Tier", "ticket_price": 1035},
                                5: {"type": "AC 3 Tier", "ticket_price": 730},
                                6: {"type": "General Coach", "ticket_price": 150}
                            }
                        },
                        3: {
                            "name": "Saurastra Janta Express",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 840},
                                2: {"type": "Second Class", "ticket_price": 165},
                                3: {"type": "Sleeper", "ticket_price": 270},
                                4: {"type": "AC 2 Tier", "ticket_price": 1035},
                                5: {"type": "AC 3 Tier", "ticket_price": 730},
                                6: {"type": "General Coach", "ticket_price": 150}
                            }
                        }
                    },
                    "Veraval": {
                        1: {
                            "name": "Tiruvananthpuram Central Express",
                            "timing": "01:00 AM - 6:30 AM",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 1155},
                                2: {"type": "Second Class", "ticket_price": 220},
                                3: {"type": "Sleeper", "ticket_price": 375},
                                4: {"type": "AC 2 Tier", "ticket_price": 1440},
                                5: {"type": "AC 3 Tier", "ticket_price": 1010},
                                6: {"type": "General Coach", "ticket_price": 205}
                            }
                        },
                        2: {
                            "name": "Veraval - Pune Express",
                            "timing": "12:55 AM - 5:02 pm",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 475},
                                2: {"type": "Second Class", "ticket_price": 90},
                                3: {"type": "Sleeper", "ticket_price": 145},
                                4: {"type": "AC 2 Tier", "ticket_price": 710},
                                5: {"type": "AC 3 Tier", "ticket_price": 505},
                                6: {"type": "General Coach", "ticket_price": 75}
                            }
                        },
                        3: {
                            "name": "Saurastra Janta Express",
                            "timing": "11:00 AM - 3:02 PM",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 475},
                                2: {"type": "Second Class", "ticket_price": 90},
                                3: {"type": "Sleeper", "ticket_price": 145},
                                4: {"type": "AC 2 Tier", "ticket_price": 710},
                                5: {"type": "AC 3 Tier", "ticket_price": 505},
                                6: {"type": "General Coach", "ticket_price": 75}
                            }
                        }
                    },
                    "Surat":{
                        1: {
                            "name": "Dadar Saurastra EXPRESS",
                            "timing": "11:00 AM - 3:02 PM",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 885},
                                2: {"type": "Second Class", "ticket_price": 170},
                                3: {"type": "Sleeper", "ticket_price": 258},
                                4: {"type": "AC 2 Tier", "ticket_price": 1090},
                                5: {"type": "AC 3 Tier", "ticket_price": 765},
                                6: {"type": "General Coach", "ticket_price": 155}
                            }
                        },
                        2: {
                            "name": "Tuticorin Vivek EXPRESS",
                            "timing": "10:00 AM - 1:00 PM",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 885},
                                2: {"type": "Second Class", "ticket_price": 170},
                                3: {"type": "Sleeper", "ticket_price": 258},
                                4: {"type": "AC 2 Tier", "ticket_price": 1090},
                                5: {"type": "AC 3 Tier", "ticket_price": 765},
                                6: {"type": "General Coach", "ticket_price": 155}
                            }
                        },
                        3: {
                            "name": "Santragachi Kavi Guru SF Express",
                            "timing": "5:00 PM - 10:00 PM",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 935},
                                2: {"type": "Second Class", "ticket_price": 185},
                                3: {"type": "Sleeper", "ticket_price": 315},
                                4: {"type": "AC 2 Tier", "ticket_price": 1135},
                                5: {"type": "AC 3 Tier", "ticket_price": 810},
                                6: {"type": "General Coach", "ticket_price": 170}
                            }
                        },
                        4: {
                            "name": "Gandhinagar Capital Intercity Express",
                            "timing": "11:00 AM - 3:02 PM",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 935},
                                2: {"type": "Second Class", "ticket_price": 185},
                                3: {"type": "Sleeper", "ticket_price": 315},
                                4: {"type": "AC 2 Tier", "ticket_price": 1135},
                                5: {"type": "AC 3 Tier", "ticket_price": 810},
                                6: {"type": "General Coach", "ticket_price": 170}
                            }
                        },
                        5: {
                            "name": "Jablpur Somanth JBP EXP",
                            "timing": "6:00 AM - 10:00 PM",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 935},
                                2: {"type": "Second Class", "ticket_price": 185},
                                3: {"type": "Sleeper", "ticket_price": 315},
                                4: {"type": "AC 2 Tier", "ticket_price": 1135},
                                5: {"type": "AC 3 Tier", "ticket_price": 810},
                                6: {"type": "General Coach", "ticket_price": 170}
                            }
                        },
                        6: {
                            "name": "Saurastra Janta Express",
                            "timing": "1:00 PM - 4:30 PM",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 935},
                                2: {"type": "Second Class", "ticket_price": 185},
                                3: {"type": "Sleeper", "ticket_price": 315},
                                4: {"type": "AC 2 Tier", "ticket_price": 1135},
                                5: {"type": "AC 3 Tier", "ticket_price": 810},
                                6: {"type": "General Coach", "ticket_price": 170}
                            }
                        }
                    },
                    "Bhavnagar":{
                        1:{
                            "name": "Bhavnagar Terminus Okha EXP",
                            "timing": "11:00 AM - 3:02 PM",
                            "coaches": {"type": "General Coach", "ticket_price": 105}
                        }
                    }
                },


                "Veraval":{
                    "Ahmedabad": {
                        1: {
                            "name": "Jabalpur SMNH JBP EXP",
                            "timing": "11:00 AM - 3:02 PM",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 840},
                                2: {"type": "Second Class", "ticket_price": 165},
                                3: {"type": "Sleeper", "ticket_price": 270},
                                4: {"type": "AC 2 Tier", "ticket_price": 1035},
                                5: {"type": "AC 3 Tier", "ticket_price": 730},
                                6: {"type": "General Coach", "ticket_price": 150}
                            }
                        },
                        2: {
                            "name": "Saurastra Janta Express",
                            "timing": "6:00 PM - 10:15 PM",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 840},
                                2: {"type": "Second Class", "ticket_price": 165},
                                3: {"type": "Sleeper", "ticket_price": 270},
                                4: {"type": "AC 2 Tier", "ticket_price": 1035},
                                5: {"type": "AC 3 Tier", "ticket_price": 730},
                                6: {"type": "General Coach", "ticket_price": 150}
                            }
                        }
                    },
                    "Surat":{
                        1: {
                            "name": "Saurastra Janta Express",
                            "timing": "11:50 AM - 12:20 AM",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 1155},
                                2: {"type": "Second Class", "ticket_price": 220},
                                3: {"type": "Sleeper", "ticket_price": 375},
                                4: {"type": "AC 2 Tier", "ticket_price": 1440},
                                5: {"type": "AC 3 Tier", "ticket_price": 1010},
                                6: {"type": "General Coach", "ticket_price": 205}
                            }
                        }
                    },
                    "Rajkot":{
                        1: {
                            "name": "Veraval - Rajkot Passenger",
                            "timing": "6:00 PM - 10:15 PM",
                            "coaches": {
                                1: {"type": "General Coach", "ticket_price": 50}
                            }
                        },
                        2: {
                            "name": "Gandhinagar Capital Intercity Express",
                            "timing": "6:00 PM - 10:15 PM",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 475},
                                2: {"type": "Second Class", "ticket_price": 90},
                                3: {"type": "Sleeper", "ticket_price": 145},
                                4: {"type": "AC 2 Tier", "ticket_price": 710},
                                5: {"type": "AC 3 Tier", "ticket_price": 505},
                                6: {"type": "General Coach", "ticket_price": 75}
                            }
                        },
                        3: {
                            "name": "Jabalpur SMNH JBP EXP",
                            "timing": "6:00 AM - 10:15 AM",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 475},
                                2: {"type": "Second Class", "ticket_price": 90},
                                3: {"type": "Sleeper", "ticket_price": 145},
                                4: {"type": "AC 2 Tier", "ticket_price": 710},
                                5: {"type": "AC 3 Tier", "ticket_price": 505},
                                6: {"type": "General Coach", "ticket_price": 75}
                            }
                        },
                        4: {
                            "name": "Saurastra Janta Express",
                            "timing": "10:00 AM - 1:15 PM",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 475},
                                2: {"type": "Second Class", "ticket_price": 90},
                                3: {"type": "Sleeper", "ticket_price": 145},
                                4: {"type": "AC 2 Tier", "ticket_price": 710},
                                5: {"type": "AC 3 Tier", "ticket_price": 505},
                                6: {"type": "General Coach", "ticket_price": 75}
                            }
                        },
                        5: {
                            "name": "Veraval - Rajkot Passenger",
                            "timing": "6:00 PM - 10:15 PM",
                            "coaches": {
                                1: {"type": "General Coach", "ticket_price": 50}
                            }
                        },
                        6: {
                            "name": "Somanth SF Express",
                            "timing": "11:30 AM - 10:15 PM",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 520},
                                2: {"type": "Second Class", "ticket_price": 105},
                                3: {"type": "Sleeper", "ticket_price": 175},
                                4: {"type": "AC 2 Tier", "ticket_price": 760},
                                5: {"type": "AC 3 Tier", "ticket_price": 555},
                                6: {"type": "General Coach", "ticket_price": 90}
                            }
                        },
                        7: {
                            "name": "Veraval - Okha Express",
                            "timing": "11:30 AM - 4:45 PM",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 520},
                                2: {"type": "Second Class", "ticket_price": 105},
                                3: {"type": "Sleeper", "ticket_price": 175},
                                4: {"type": "AC 2 Tier", "ticket_price": 760},
                                5: {"type": "AC 3 Tier", "ticket_price": 555},
                                6: {"type": "General Coach", "ticket_price": 90}
                            }
                        }
                    },
                    "Bhavnagar":{
                        1:{
                            "name": "Veraval - Bhavnagar Terminus Passenger",
                            "timing": "11:30 AM - 4:45 PM",
                            "coaches":{
                                1: {"type": "General Coach", "ticket_price": 65}
                            }
                        }
                    }
                },


                "Surat":{
                    "Veraval":{
                        1: {
                        "name": "Thiruvananthapuram Central Express",
                        "timing": "6:50 AM - 7:24 PM",
                        "coaches": {
                            1: {"type": "First Class", "ticket_price": 1155},
                            2: {"type": "Second Class", "ticket_price": 220},
                            3: {"type": "Sleeper", "ticket_price": 375},
                            4: {"type": "AC 2 Tier", "ticket_price": 1440},
                            5: {"type": "AC 3 Tier", "ticket_price": 1010},
                            6: {"type": "General Coach", "ticket_price": 205}
                        }
                    },
                        2: {
                            "name": "Veraval - Pune Express",
                            "timing": "11:05 AM - 11:51 PM",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 1155},
                                2: {"type": "Second Class", "ticket_price": 220},
                                3: {"type": "Sleeper", "ticket_price": 375},
                                4: {"type": "AC 2 Tier", "ticket_price": 1440},
                                5: {"type": "AC 3 Tier", "ticket_price": 1010},
                                6: {"type": "General Coach", "ticket_price": 205}
                            }
                        },
                        3: {
                            "name": "Saurashtra Janta Express",
                            "timing": "11:50 AM - 12:20 AM",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 1155},
                                2: {"type": "Second Class", "ticket_price": 220},
                                3: {"type": "Sleeper", "ticket_price": 375},
                                4: {"type": "AC 2 Tier", "ticket_price": 1440},
                                5: {"type": "AC 3 Tier", "ticket_price": 1010},
                                6: {"type": "General Coach", "ticket_price": 205}
                            }
                        },
                        4: {
                            "name": "Bandra Terminus Weekly Express",
                            "timing": "5:15 PM - 11:30 AM",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 1195},
                                2: {"type": "Second Class", "ticket_price": 230},
                                3: {"type": "Sleeper", "ticket_price": 385},
                                4: {"type": "AC 2 Tier", "ticket_price": 1485},
                                5: {"type": "AC 3 Tier", "ticket_price": 1040},
                                6: {"type": "General Coach", "ticket_price": 215}
                            }
                        }
                    },
                    "Ahmedabad":{
                        1: {
                            "name": "Lokshakti Express",
                            "timing": "12:37 AM - 4:20 AM",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 580},
                                2: {"type": "Second Class", "ticket_price": 120},
                                3: {"type": "Sleeper", "ticket_price": 205},
                                4: {"type": "AC 2 Tier", "ticket_price": 760},
                                5: {"type": "AC 3 Tier", "ticket_price": 555},
                                6: {"type": "General Coach", "ticket_price": 105}
                            }
                        },
                        2: {
                            "name": "Amrapur Aravali Express",
                            "timing": "12:55 AM - 4:30 AM",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 535},
                                2: {"type": "Second Class", "ticket_price": 105},
                                3: {"type": "Sleeper", "ticket_price": 175},
                                4: {"type": "AC 2 Tier", "ticket_price": 710},
                                5: {"type": "AC 3 Tier", "ticket_price": 505},
                                6: {"type": "General Coach", "ticket_price": 90}
                            }
                        },
                        3: {
                            "name": "Saurastra Mail",
                            "timing": "1:07 AM - 5:00 AM",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 580},
                                2: {"type": "Second Class", "ticket_price": 105},
                                3: {"type": "Sleeper", "ticket_price": 205},
                                4: {"type": "AC 2 Tier", "ticket_price": 760},
                                5: {"type": "AC 3 Tier", "ticket_price": 555},
                                6: {"type": "General Coach", "ticket_price": 105}
                            }
                        },
                        4: {
                            "name": "Gujrat Mail",
                            "timing": "1:19 AM - 5:50 AM",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 580},
                                2: {"type": "Second Class", "ticket_price": 120},
                                3: {"type": "Sleeper", "ticket_price": 205},
                                4: {"type": "AC 2 Tier", "ticket_price": 760},
                                5: {"type": "AC 3 Tier", "ticket_price": 555},
                                6: {"type": "General Coach", "ticket_price": 105}
                            }
                        }
                    },
                    "Rajkot":{
                        1: {
                            "name": "Saurastra Mail",
                            "timing": "1:07 AM - 9:26 AM",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 935},
                                2: {"type": "Second Class", "ticket_price": 185},
                                3: {"type": "Sleeper", "ticket_price": 315},
                                4: {"type": "AC 2 Tier", "ticket_price": 1135},
                                5: {"type": "AC 3 Tier", "ticket_price": 810},
                                6: {"type": "General Coach", "ticket_price": 170}
                            }
                        },
                        2: {
                            "name": "Porbandar Saurastra EXP",
                            "timing": "3:00 PM - 12:55 AM",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 885},
                                2: {"type": "Second Class", "ticket_price": 170},
                                3: {"type": "Sleeper", "ticket_price": 285},
                                4: {"type": "AC 2 Tier", "ticket_price": 1090},
                                5: {"type": "AC 3 Tier", "ticket_price": 765},
                                6: {"type": "General Coach", "ticket_price": 155}
                            }
                        },
                        3: {
                            "name": "Sauratsra Janta Express",
                            "timing": "5:45 PM - 2:20 AM",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 885},
                                2: {"type": "Second Class", "ticket_price": 170},
                                3: {"type": "Sleeper", "ticket_price": 285},
                                4: {"type": "AC 2 Tier", "ticket_price": 1090},
                                5: {"type": "AC 3 Tier", "ticket_price": 765},
                                6: {"type": "General Coach", "ticket_price": 155}
                            }
                        }
                    },
                    "Bhavnagar":{
                        1: {
                            "name": "Bhavnagar Terminus",
                            "timing": "2:50 AM - 12:25 PM",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 975},
                                2: {"type": "Second Class", "ticket_price": 185},
                                3: {"type": "Sleeper", "ticket_price": 315},
                                4: {"type": "AC 2 Tier", "ticket_price": 1215},
                                5: {"type": "AC 3 Tier", "ticket_price": 855},
                                6: {"type": "General Coach", "ticket_price": 170}
                            }
                        },
                        2: {
                            "name": "Bhavnagar Terminus SF Express",
                            "timing": "11:07 PM - 8:05 AM",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 1020},
                                2: {"type": "Second Class", "ticket_price": 200},
                                3: {"type": "Sleeper", "ticket_price": 345},
                                4: {"type": "AC 2 Tier", "ticket_price": 1265},
                                5: {"type": "AC 3 Tier", "ticket_price": 905},
                                6: {"type": "General Coach", "ticket_price": 185}
                            }
                        },
                        3: {
                            "name": "Palitana Weekly SF Express",
                            "timing": "8:28 PM - 4:32 AM",
                            "coaches": {
                                1: {"type": "First Class", "ticket_price": 960},
                                2: {"type": "Second Class", "ticket_price": 190},
                                3: {"type": "Sleeper", "ticket_price": 325},
                                4: {"type": "AC 2 Tier", "ticket_price": 1170},
                                5: {"type": "AC 3 Tier", "ticket_price": 835},
                                6: {"type": "General Coach", "ticket_price": 175}
                            }
                        }
                    }
                },


                "Ahmedabad":{
                    "Veraval":{
                        1: {
                            "name": "Veraval Weekly Express",
                            "timing": "3:15 AM - 1:10 PM",
                            "coaches": {
                                1: {"type": "FC - First Class", "ticket_price": 885},
                                2: {"type": "2S - Second Class", "ticket_price": 170},
                                3: {"type": "SL - Sleeper", "ticket_price": 285},
                                4: {"type": "2A - AC 2 Tier", "ticket_price": 1090},
                                5: {"type": "3A - AC 3 Tier", "ticket_price": 765},
                                6: {"type": "General Coach", "ticket_price": 155}
                            }
                        },
                        2: {
                            "name": "Veraval Express",
                            "timing": "6:50 AM - 3:35 PM",
                            "coaches": {
                                1: {"type": "FC - First Class", "ticket_price": 840},
                                2: {"type": "2S - Second Class", "ticket_price": 165},
                                3: {"type": "SL - Sleeper", "ticket_price": 270},
                                4: {"type": "2A - AC 2 Tier", "ticket_price": 1035},
                                5: {"type": "3A - AC 3 Tier", "ticket_price": 730},
                                6: {"type": "General Coach", "ticket_price": 150}
                            }
                        },
                        3: {
                            "name": "Saurastra Janta Express",
                            "timing": "10:20 PM - 7:10 AM",
                            "coaches": {
                                1: {"type": "FC - First Class", "ticket_price": 840},
                                2: {"type": "2S - Second Class", "ticket_price": 165},
                                3: {"type": "SL - Sleeper", "ticket_price": 285},
                                4: {"type": "2A - AC 2 Tier", "ticket_price": 1035},
                                5: {"type": "3A - AC 3 Tier", "ticket_price": 730},
                                6: {"type": "General Coach", "ticket_price": 150}
                            }
                        }
                    },
                    "Rajkot":{
                        1: {
                            "name": "Okha Dwarka SF Express",
                            "timing": "12:55 AM - 5:02 AM",
                            "coaches": {
                                1: {"type": "FC - First Class", "ticket_price": 610},
                                2: {"type": "2S - Second Class", "ticket_price": 125},
                                3: {"type": "SL - Sleeper", "ticket_price": 215},
                                4: {"type": "2A - AC 2 Tier", "ticket_price": 760},
                                5: {"type": "3A - AC 3 Tier", "ticket_price": 555},
                                6: {"type": "General Coach", "ticket_price": 110}
                            }
                        },
                        2: {
                            "name": "Saurastra Mial",
                            "timing": "5:10 AM - 9:26 AM",
                            "coaches": {
                                1: {"type": "FC - First Class", "ticket_price": 840},
                                2: {"type": "2S - Second Class", "ticket_price": 165},
                                3: {"type": "SL - Sleeper", "ticket_price": 270},
                                4: {"type": "2A - AC 2 Tier", "ticket_price": 1035},
                                5: {"type": "3A - AC 3 Tier", "ticket_price": 730},
                                6: {"type": "General Coach", "ticket_price": 150}
                            }
                        },
                        3: {
                            "name": "Jamnagar Intercity Exp",
                            "timing": "5:40 PM - 9:42 AM",
                            "coaches": {
                                1: {"type": "FC - First Class", "ticket_price": 610},
                                2: {"type": "2S - Second Class", "ticket_price": 125},
                                3: {"type": "SL - Sleeper", "ticket_price": 215},
                                4: {"type": "2A - AC 2 Tier", "ticket_price": 760},
                                5: {"type": "3A - AC 3 Tier", "ticket_price": 555},
                                6: {"type": "General Coach", "ticket_price": 110}
                            }
                        }
                    },
                    "Surat":{
                        1: {
                            "name": "Howrah SF Express",
                            "timing": "12:25 AM - 4:26 AM",
                            "coaches": {
                                1: {"type": "FC - First Class", "ticket_price": 580},
                                2: {"type": "2S - Second Class", "ticket_price": 120},
                                3: {"type": "SL - Sleeper", "ticket_price": 205},
                                4: {"type": "2A - AC 2 Tier", "ticket_price": 760},
                                5: {"type": "3A - AC 3 Tier", "ticket_price": 555},
                                6: {"type": "General Coach", "ticket_price": 105}
                            }
                        },
                        2: {
                            "name": "Kutch SF Express",
                            "timing": "2:55 AM - 6:45 AM",
                            "coaches": {
                                1: {"type": "FC - First Class", "ticket_price": 580},
                                2: {"type": "2S - Second Class", "ticket_price": 120},
                                3: {"type": "SL - Sleeper", "ticket_price": 205},
                                4: {"type": "2A - AC 2 Tier", "ticket_price": 760},
                                5: {"type": "3A - AC 3 Tier", "ticket_price": 555},
                                6: {"type": "General Coach", "ticket_price": 105}
                            }
                        },
                        3: {
                            "name": "Suryanagari SF Express",
                            "timing": "3:50 AM - 7:22 AM",
                            "coaches": {
                                1: {"type": "FC - First Class", "ticket_price": 580},
                                2: {"type": "2S - Second Class", "ticket_price": 120},
                                3: {"type": "SL - Sleeper", "ticket_price": 205},
                                4: {"type": "2A - AC 2 Tier", "ticket_price": 760},
                                5: {"type": "3A - AC 3 Tier", "ticket_price": 555},
                                6: {"type": "General Coach", "ticket_price": 105}
                            }
                        },
                        4: {
                            "name": "Karnavati Express",
                            "timing": "5:00 AM - 8:08 AM",
                            "coaches": {
                                1: {"type": "FC - First Class", "ticket_price": 580},
                                2: {"type": "2S - Second Class", "ticket_price": 120},
                                3: {"type": "SL - Sleeper", "ticket_price": 205},
                                4: {"type": "2A - AC 2 Tier", "ticket_price": 760},
                                5: {"type": "3A - AC 3 Tier", "ticket_price": 555},
                                6: {"type": "General Coach", "ticket_price": 105}
                            }
                        }
                    },
                    "Bhavnagar":{
                        1: {
                            "name": "Bhavnagar Terminus SF Express",
                            "timing": "2:50 AM - 8:05 AM",
                            "coaches": {
                                1: {"type": "FC - First Class", "ticket_price": 680},
                                2: {"type": "2S - Second Class", "ticket_price": 140},
                                3: {"type": "SL - Sleeper", "ticket_price": 235},
                                4: {"type": "2A - AC 2 Tier", "ticket_price": 760},
                                5: {"type": "3A - AC 3 Tier", "ticket_price": 555},
                                6: {"type": "General Coach", "ticket_price": 125}
                            }
                        },
                        2: {
                            "name": "Bhavnagar Terminus BVC Intercity",
                            "timing": "4:10 PM - 8:55 PM",
                            "coaches": {
                                1: {"type": "FC - First Class", "ticket_price": 630},
                                2: {"type": "2S - Second Class", "ticket_price": 130},
                                3: {"type": "SL - Sleeper", "ticket_price": 220},
                                4: {"type": "2A - AC 2 Tier", "ticket_price": 760},
                                5: {"type": "3A - AC 3 Tier", "ticket_price": 555},
                                6: {"type": "General Coach", "ticket_price": 115}
                            }
                        }
                    }
                },


                "Bhavnagar":{
                    "Veraval":{
                        1: {
                            "name": "Bhavnagar Terminus - Veraval Passenger",
                            "timing": "4:40 AM - 11:30 AM",
                            "coaches": {
                                1: {"type": "General Coach", "ticket_price": 65}
                            }
                        }
                    },
                    "Ahmedabad":{
                        1: {
                            'name': "Bandra Terminus Express",
                            'timing': "6:30 PM - 11:35 PM",
                            'coaches': {
                                1: {"type": "FC - First Class", "ticket_price": 6380},
                                2: {"type": "2S - Second Class", "ticket_price": 140},
                                3: {"type": "SL - Sleeper", "ticket_price": 235},
                                4: {"type": "2A - AC 2 Tier", "ticket_price": 760},
                                5: {"type": "3A - AC 3 Tier", "ticket_price": 555},
                                6: {"type": "General Coach", "ticket_price": 125}
                            }
                        },
                        2: {
                            'name': "Sabarmati BG",
                            'timing': "6:00 AM - 10:30 AM",
                            'coaches': {
                                1: {"type": "FC - First Class", "ticket_price": 630},
                                2: {"type": "2S - Second Class", "ticket_price": 130},
                                3: {"type": "SL - Sleeper", "ticket_price": 220},
                                4: {"type": "2A - AC 2 Tier", "ticket_price": 760},
                                5: {"type": "3A - AC 3 Tier", "ticket_price": 555},
                                6: {"type": "General Coach", "ticket_price": 115}
                            }
                        }
                    },
                    "Surat":{
                        1: {
                        'name': "Kochiveli Express",
                        'timing': "10:15 AM - 7:24 PM",
                        'coaches': {
                            1: {"type": "FC - First Class", "ticket_price": 1020},
                            2: {"type": "2S - Second Class", "ticket_price": 185},
                            3: {"type": "SL - Sleeper", "ticket_price": 345},
                            4: {"type": "2A - AC 2 Tier", "ticket_price": 1265},
                            5: {"type": "3A - AC 3 Tier", "ticket_price": 905},
                            6: {"type": "General Coach", "ticket_price": 185}
                        }
                    },
                        2: {
                            'name': "Bandra Terminus SF Express",
                            'timing': "6:30 PM - 3:24 AM",
                            'coaches': {
                                1: {"type": "FC - First Class", "ticket_price": 1020},
                                2: {"type": "2S - Second Class", "ticket_price": 200},
                                3: {"type": "SL - Sleeper", "ticket_price": 345},
                                4: {"type": "2A - AC 2 Tier", "ticket_price": 1265},
                                5: {"type": "3A - AC 3 Tier", "ticket_price": 175},
                                6: {"type": "General Coach", "ticket_price": 175}
                            }
                        },
                        3: {
                            'name': "Bandra Terminus Weekly SF Express",
                            'timing': "8:58 PM - 5:25 AM",
                            'coaches': {
                                1: {"type": "FC - First Class", "ticket_price": 960},
                                2: {"type": "2S - Second Class", "ticket_price": 190},
                                3: {"type": "SL - Sleeper", "ticket_price": 325},
                                4: {"type": "2A - AC 2 Tier", "ticket_price": 1170},
                                5: {"type": "3A - AC 3 Tier", "ticket_price": 835},
                                6: {"type": "General Coach", "ticket_price": 175}
                            }
                        }

            },
                    "Rajkot":{
                        'name': "Surendranagar Okha EXP",
                        'timing': "10:10 PM - 6:00 AM",
                        'coaches':{
                            1: {"type": "General Coach", "ticket_price": 105}
                        }

                    }
                }
            }

            self.create_widgets()

        def create_widgets(self):
            title_label = tk.Label(self.root, text="Train Ticket Booking", font=("Helvetica", 18, "bold"), bg="#4682B4",fg="white")
            title_label.pack(pady=10)

            # From Station Frame
            from_station_frame = tk.Frame(self.root, bg="#ADD8E6")
            from_station_frame.pack(pady=10)

            from_station_label = tk.Label(from_station_frame, text="From Station:", font=("Helvetica", 12, "bold"),
                                          bg="#ADD8E6")
            from_station_label.grid(row=0, column=0, padx=10)

            self.from_station_var = StringVar(value="Select a Station")
            self.from_station_menu = ttk.Combobox(from_station_frame, textvariable=self.from_station_var,
                                                  state="readonly", font=("Helvetica", 10))
            self.from_station_menu['values'] = list(self.trains.keys())
            self.from_station_menu.grid(row=0, column=1)
            self.from_station_menu.bind("<<ComboboxSelected>>", self.update_to_station_menu)

            # To Station Frame
            to_station_frame = tk.Frame(self.root, bg="#ADD8E6")
            to_station_frame.pack(pady=10)

            to_station_label = tk.Label(to_station_frame, text="To Station:", font=("Helvetica", 12, "bold"),
                                        bg="#ADD8E6")
            to_station_label.grid(row=0, column=0, padx=10)

            self.to_station_var = StringVar(value="Select a Station")
            self.to_station_menu = ttk.Combobox(to_station_frame, textvariable=self.to_station_var, state="readonly",
                                                font=("Helvetica", 10))
            self.to_station_menu.grid(row=0, column=1)
            self.to_station_menu.bind("<<ComboboxSelected>>", self.update_train_menu)

            # Train Selection Frame
            train_frame = tk.Frame(self.root, bg="#ADD8E6")
            train_frame.pack(pady=10)

            tk.Label(train_frame, text="Select Train:", font=("Helvetica", 12, "bold"), bg="#ADD8E6").grid(row=0,column=0,padx=10)

            self.train_var = StringVar(value="Select a Train")
            self.train_menu = ttk.Combobox(train_frame, textvariable=self.train_var, state='readonly',
                                           font=("Helvetica", 10), width=30)
            self.train_menu.grid(row=0, column=1)
            self.train_menu.bind("<<ComboboxSelected>>", self.update_coach_menu)

            # Timing Display
            self.timing_label = tk.Label(train_frame, text="Timing: ", font=("Arial", 12), bg="#ADD8E6")
            self.timing_label.grid(row=1, column=0, columnspan=2, pady=10)

            # Coach Selection Frame
            coach_frame = tk.Frame(self.root, bg="#ADD8E6")
            coach_frame.pack(pady=10)

            coach_label = tk.Label(coach_frame, text="Select Coach:", font=("Helvetica", 12, "bold"), bg="#ADD8E6")
            coach_label.grid(row=0, column=0, padx=10)

            self.coach_var = StringVar(value="Select a Coach")
            self.coach_menu = ttk.Combobox(coach_frame, textvariable=self.coach_var, state='readonly',
                                           font=("Helvetica", 10))
            self.coach_menu.grid(row=0, column=1)
            self.coach_menu.bind("<<ComboboxSelected>>", self.update_single_price)

            # Ticket Frame
            ticket_frame = tk.Frame(self.root, bg="#ADD8E6")
            ticket_frame.pack(pady=10)

            ticket_label = tk.Label(ticket_frame, text="Number of Tickets:", font=("Helvetica", 12, "bold"),
                                    bg="#ADD8E6")
            ticket_label.grid(row=0, column=0, padx=10)

            self.num_tickets_var = IntVar(value=1)
            self.num_tickets_spinbox = tk.Spinbox(ticket_frame, from_=1, to=10, textvariable=self.num_tickets_var,
                                                  width=5, font=("Helvetica", 10))
            self.num_tickets_spinbox.grid(row=0, column=1)

            self.single_price_label = tk.Label(self.root, text="Single Ticket Price: ", font=("Helvetica", 12),
                                               bg="#ADD8E6")
            self.single_price_label.pack(pady=10)

            book_button = tk.Button(self.root, text="Book Ticket", font=("Helvetica", 12, "bold"), bg="#32CD32",
                                    fg="white",
                                    relief="raised", command=self.book_ticket)
            book_button.pack(pady=20)

        def calculate_total_price(self, ticket_price, num_tickets):
            return ticket_price * num_tickets

        def update_to_station_menu(self, event):
            selected_from_station = self.from_station_var.get()
            if selected_from_station in self.trains:
                self.to_station_menu['values'] = list(self.trains[selected_from_station].keys())
                self.to_station_menu.state(['!disabled'])
                self.to_station_menu.set("Select a To Station")
                self.train_menu.set("Select a Train")
                self.train_menu.state(['disabled'])
                self.coach_menu.set("Select a Coach")
                self.coach_menu.state(['disabled'])
                self.single_price_label.config(text="Single Ticket Price: ")
            else:
                self.to_station_menu['values'] = []
                self.to_station_menu.state(['disabled'])

        def update_train_menu(self, event):
            selected_from_station = self.from_station_var.get()
            selected_to_station = self.to_station_var.get()

            if selected_from_station in self.trains and selected_to_station in self.trains[selected_from_station]:
                trains = self.trains[selected_from_station][selected_to_station]
                self.train_menu['values'] = [train['name'] for train in trains.values()]
                self.train_menu.state(['!disabled'])
                self.train_menu.set("Select a Train")
                self.coach_menu.set("Select a Coach")
                self.coach_menu.state(['disabled'])
                self.single_price_label.config(text="Single Ticket Price: ")
            else:
                self.train_menu['values'] = []
                self.train_menu.state(['disabled'])
                self.coach_menu.set("Select a Coach")
                self.coach_menu.state(['disabled'])
                self.single_price_label.config(text="Single Ticket Price: ")

        def update_coach_menu(self, event):
            selected_from_station = self.from_station_var.get()
            selected_to_station = self.to_station_var.get()
            selected_train_name = self.train_var.get()

            if "Select a Train" in selected_train_name:
                self.timing_label.config(text="Timing: ")
                return

            trains = self.trains[selected_from_station][selected_to_station]
            selected_train_info = None

            for train in trains.values():
                if train['name'] == selected_train_name:
                    selected_train_info = train
                    break

            if selected_train_info:
                coaches = selected_train_info["coaches"]
                self.coach_menu['values'] = [coach["type"] for coach in coaches.values()]
                self.coach_menu.state(['!disabled'])
                self.coach_menu.set("Select a Coach")

                timing = selected_train_info.get("timing", "Not Available")
                self.timing_label.config(text=f"Timing: {timing}")

        def update_single_price(self, event):
            selected_from_station = self.from_station_var.get()
            selected_to_station = self.to_station_var.get()
            selected_train_name = self.train_var.get()
            selected_coach_type = self.coach_var.get()

            if "Select a Coach" in selected_coach_type or "Select a Train" in selected_train_name:
                return

            trains = self.trains[selected_from_station][selected_to_station]
            selected_train_info = None
            for train in trains.values():
                if train['name'] == selected_train_name:
                    selected_train_info = train
                    break

            coaches = selected_train_info["coaches"]
            selected_coach_info = None
            for coach in coaches.values():
                if coach["type"] == selected_coach_type:
                    selected_coach_info = coach
                    break

            ticket_price = selected_coach_info["ticket_price"]
            self.single_price_label.config(text=f"Single Ticket Price: ₹ {ticket_price}")

        def book_ticket(self):
            selected_from_station = self.from_station_var.get()
            selected_to_station = self.to_station_var.get()
            selected_train_name = self.train_var.get()
            selected_coach_type = self.coach_var.get()
            num_tickets = self.num_tickets_var.get()

            if "Select" in selected_from_station or "Select" in selected_to_station or "Select" in selected_train_name or "Select" in selected_coach_type:
                missing_fields = []
                if "Select" in selected_from_station:
                    missing_fields.append("From Station")
                if "Select" in selected_to_station:
                    missing_fields.append("To Station")
                if "Select" in selected_train_name:
                    missing_fields.append("Train")
                if "Select" in selected_coach_type:
                    missing_fields.append("Coach")

                messagebox.showerror("Error", f"Please select all fields: {', '.join(missing_fields)}.")
                return


            trains = self.trains[selected_from_station][selected_to_station]
            selected_train_info = None
            for train in trains.values():
                if train['name'] == selected_train_name:
                    selected_train_info = train
                    break


            coaches = selected_train_info["coaches"]
            selected_coach_info = None
            for coach in coaches.values():
                if coach["type"] == selected_coach_type:
                    selected_coach_info = coach
                    break

            ticket_price = selected_coach_info["ticket_price"]
            total_price = self.calculate_total_price(ticket_price, num_tickets)

            messagebox.showinfo("Booking Confirmed", f"Your booking is confirmed!\nTotal Ticket Price: ₹ {total_price}")

    root = tk.Tk()
    app = TrainApp(root)
    root.mainloop()

if __name__ == "__main__":
    run()