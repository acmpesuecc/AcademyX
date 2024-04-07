import React from 'react';
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from '@/components/ui/accordion';

const courseData = {
  title: 'The Art of Photography',
  modules: [
    {
      title: 'Introduction to Photography',
      lessons: [
        { title: 'Understanding Camera Basics', duration: '00:15:00' },
        { title: 'Aperture, Shutter Speed & ISO', duration: '00:20:00' },
        { title: 'Composition Techniques', duration: '00:25:00' },
      ],
    },
    {
      title: 'Essential Photography Skills',
      lessons: [
        { title: 'Mastering Lighting', duration: '00:30:00' },
        { title: 'Shooting in Different Environments', duration: '00:25:00' },
        { title: 'Capturing Portraits', duration: '00:20:00' },
      ],
    },
  ],
};

export default function CourseLandingPage() {
  const totalModules = courseData.modules.length;
  const totalLessons = courseData.modules.reduce(
    (acc, module) => acc + module.lessons.length,
    0
  );
  const totalDuration = courseData.modules.reduce(
    (acc, module) =>
      acc +
      module.lessons.reduce(
        (lessonAcc, lesson) =>
          lessonAcc + convertTimeToSeconds(lesson.duration),
        0
      ),
    0
  );

  function convertTimeToSeconds(time: string) {
    const parts = time.split(':');
    return (
      parseInt(parts[0]) * 60 * 60 +
      parseInt(parts[1]) * 60 +
      parseInt(parts[2])
    );
  }

  function formatTime(seconds: number) {
    const hours = Math.floor(seconds / (60 * 60));
    const minutes = Math.floor((seconds % (60 * 60)) / 60);
    const secondsLeft = seconds % 60;
    return `${hours.toString().padStart(2, '0')}:${minutes
      .toString()
      .padStart(2, '0')}:${secondsLeft.toString().padStart(2, '0')}`;
  }

  return (
    <div className="p-4">
      <h1 className="text-2xl font-semibold mb-4">{courseData.title}</h1>
      <p className="mb-4">
        {totalModules} modules • {totalLessons} lectures •{' '}
        {formatTime(totalDuration)} total length
      </p>

      <Accordion type="single" collapsible>
        {courseData.modules.map((module) => (
          <AccordionItem key={module.title} value={module.title}>
            <AccordionTrigger className="font-semibold">
              {module.title}
            </AccordionTrigger>
            <AccordionContent>
              <ul className="list-disc ml-4">
                {module.lessons.map((lesson) => (
                  <li key={lesson.title}>
                    {lesson.title} ({lesson.duration})
                  </li>
                ))}
              </ul>
            </AccordionContent>
          </AccordionItem>
        ))}
      </Accordion>
    </div>
  );
}
