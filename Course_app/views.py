from django.shortcuts import render, get_object_or_404, redirect
from .models import Card_list, Topic , TopicDetail, MCQ, FillInTheBlank


# View for displaying all cards
def card_list_view(request):
    cards = Card_list.objects.all()  # Fetch all cards
    return render(request, 'Courses/Courses_card.html', {'cards': cards})

# View for displaying topic details with MCQs and Fill-in-the-blank questions
def topic_detail_view(request, card_id, topic_id=None):
    card = get_object_or_404(Card_list, pk=card_id)
    topics = Topic.objects.filter(card_list=card)
    selected_topic = get_object_or_404(Topic, pk=topic_id) if topic_id else topics.first()

    topic_detail = selected_topic.detail
    mcqs = MCQ.objects.filter(topic_detail=topic_detail)
    fill_blanks = FillInTheBlank.objects.filter(topic_detail=topic_detail)

    # Process form submission
    if request.method == 'POST':
        mcq_score, fill_score = 0, 0

        # Evaluate MCQs
        for mcq in mcqs:
            user_answer = request.POST.get(f'mcq_{mcq.id}')
            if user_answer == mcq.correct_option:
                mcq_score += 1

        # Evaluate Fill-in-the-blanks
        for fb in fill_blanks:
            user_answer = request.POST.get(f'fill_{fb.id}', '').strip().lower()
            if user_answer == fb.answer.lower():
                fill_score += 1

        total_score = mcq_score + fill_score
        message = f"Success! You scored {total_score} out of {len(mcqs) + len(fill_blanks)}."

        return render(request, 'Courses/result.html', {'message': message})

    return render(request, 'Courses/Course_detail_page.html', {
        'card': card,
        'topics': topics,
        'selected_topic': selected_topic,
        'mcqs': mcqs,
        'fill_blanks': fill_blanks,
    })