from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings

SLACK_VERIFICATION_TOKEN = getattr(settings, 'SLACK_VERIFICATION_TOKEN', None)

class Events(APIView):
    def post(self, request, *args, **kwargs):

        print('STARTS ==>')
        slack_message = request.data
        if slack_message.get('token') != SLACK_VERIFICATION_TOKEN:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return Response(status=status.HTTP_200_OK)

        # verification challenge
        if slack_message.get('type') == 'url_verification':  #
            print (slack_message,status.HTTP_200_OK)
            return Response(data=slack_message,  #
                            status=status.HTTP_200_OK)  #

        return Response(status=status.HTTP_200_OK)

        # greet bot
        if 'event' in slack_message:  # 4
            event_message = slack_message.get('event')  #

            # ignore bot's own message
            if event_message.get('subtype') == 'bot_message':  # 5
                return Response(status=status.HTTP_200_OK)  #

            # process user's message
            user = event_message.get('user')  # 6
            text = event_message.get('text')  #
            channel = event_message.get('channel')  #
            bot_text = 'Hi <@{}> :wave:'.format(user)  #
            if 'hi' in text.lower():  # 7
                Client.api_call(method='chat.postMessage',  # 8
                                channel=channel,  #
                                text=bot_text)  #
                return Response(status=status.HTTP_200_OK)  # 9

        return Response(status=status.HTTP_200_OK)