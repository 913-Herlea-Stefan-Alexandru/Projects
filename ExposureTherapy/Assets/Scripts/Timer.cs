using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Timer : MonoBehaviour
{
    public float targetTime = 10.0f;
    public Canvas proceedText;
    public Canvas fade;

    bool timerRunning;

    private void Awake()
    {
        timerRunning = false;
    }

    private void Start()
    {
        proceedText.enabled = false;
    }

    void Update()
    {
        if (timerRunning)
        {
            targetTime -= Time.deltaTime;

            if (targetTime <= 0.0f)
            {
                timerEnded();
            }
        }
    }

    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            startTimer();
        }
    }

    public void startTimer()
    {
        timerRunning = true;
    }

    void timerEnded()
    {
        timerRunning = false;
        proceedText.enabled = true;
        fade.enabled = true;
        Destroy(gameObject);
    }
}
