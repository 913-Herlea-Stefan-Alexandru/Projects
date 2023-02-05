using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;

public class ShowText : MonoBehaviour
{
    [SerializeField]
    private Canvas yourText; // Insert your text object inside unity inspector

    void Start()
    {
        yourText.enabled = false; // You may need to use .SetActive(false);
    }

    private void OnCollisionEnter(Collision collision)
    {
        if (collision.gameObject.tag == "Player")
        {
            // This is where you make your text object appear on screen
            yourText.enabled = true; // May need to use .SetActive(true);
        }
    }

    private void OnCollisionExit(Collision collision)
    {
        // Here is where you make the text disappear off screen
        if (collision.gameObject.tag == "Player")
        {
            yourText.enabled = false; // May need to use .SetActive(false);
        }
    }
}
