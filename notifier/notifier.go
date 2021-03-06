package notifier

import "fmt"

//TODO: logging

/*
	Msg's struct to control notifer
*/
type NotifierMsg struct {

	/*
		   Message Type. It copies most of the messages types from adapter Could be:
			"AddPeer", - add external point of notification (aka bgp peer in our cases; we dont have
				any other way to notify so far; mb going to add "exec external script" notifier)
			"RemovePeer", - remove external point of notificatio
	*/
	Type string

	/*
		data could be vip (v4/v6) address etc
	*/
	Data string
}

/*
	General notifier configuration
*/
type NotifierConfig struct {
	Type string
	//if notifier is BGP; bgp related configuration
	ASN            uint32
	ListenLocal    bool
	NeighboursList []string
}

func Notifier(msgChan chan NotifierMsg, responseChan chan NotifierMsg,
	notifierConfig NotifierConfig) {
	//TODO: ExecExcternal shell script; should be easy to implement
	switch notifierConfig.Type {
	case "bgp":
		go BGPNotifier(msgChan, responseChan, notifierConfig)
	case "dummy":
		go DummyNotifier(msgChan)
	default:
		go SilentNotifier(msgChan)
	}
}

func DummyNotifier(msgChan chan NotifierMsg) {
	for {
		msg := <-msgChan
		fmt.Printf("Dummy Notifier: %#v\n", msg)
	}
}

func SilentNotifier(msgChan chan NotifierMsg) {
	for {
		<-msgChan
	}
}
